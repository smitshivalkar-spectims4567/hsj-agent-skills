#!/usr/bin/env node
/** Small zero-dependency catalog for HSJ's Markdown content. */
import { readdir, readFile, stat } from 'node:fs/promises';
import { join, relative, resolve } from 'node:path';

const root = resolve(new URL('..', import.meta.url).pathname);
const agencyRoot = join(root, 'agency');
const divisions = new Set(['academic','design','engineering','finance','game-development','gis','healthcare','marketing','paid-media','product','project-management','research','sales','security','spatial-computing','specialized','support','testing']);

async function walk(dir) {
  const entries = await readdir(dir, { withFileTypes: true });
  const result = [];
  for (const entry of entries) {
    if (entry.name === '.git') continue;
    const path = join(dir, entry.name);
    if (entry.isDirectory()) result.push(...await walk(path));
    else result.push(path);
  }
  return result;
}

function frontmatter(text) {
  const match = text.match(/^---\n([\s\S]*?)\n---/);
  const data = {};
  for (const line of match?.[1]?.split('\n') ?? []) {
    const separator = line.indexOf(':');
    if (separator > 0) data[line.slice(0, separator).trim()] = line.slice(separator + 1).trim().replace(/^"|"$/g, '');
  }
  return data;
}

const files = await walk(agencyRoot);
const agents = files.filter((path) => path.endsWith('.md') && divisions.has(relative(agencyRoot, path).split('/')[0]) && !path.endsWith('/README.md'));
const [command, ...args] = process.argv.slice(2);
if (command === 'list') {
  console.log(`${agents.length} agency specialists`);
  for (const path of agents) {
    const data = frontmatter(await readFile(path, 'utf8'));
    console.log(`${relative(root, path)}\t${data.name ?? relative(agencyRoot, path)}\t${data.description ?? ''}`);
  }
} else if (command === 'search') {
  const terms = args.join(' ').toLowerCase().split(/\s+/).filter(Boolean);
  const hits = [];
  for (const path of agents) {
    const text = await readFile(path, 'utf8');
    if (terms.every((term) => text.toLowerCase().includes(term))) hits.push(path);
  }
  console.log(`${hits.length} matches`);
  for (const path of hits) {
    const data = frontmatter(await readFile(path, 'utf8'));
    console.log(`${relative(root, path)}\t${data.name ?? ''}\t${data.description ?? ''}`);
  }
} else if (command === 'inventory') {
  const all = await walk(root);
  const counts = new Map();
  for (const path of all) {
    const extension = path.includes('.') ? path.slice(path.lastIndexOf('.')) : '[no extension]';
    counts.set(extension, (counts.get(extension) ?? 0) + 1);
  }
  for (const [extension, count] of [...counts].sort((a, b) => b[1] - a[1])) console.log(`${extension}\t${count}`);
} else {
  console.log('Usage: node scripts/hsj.mjs list|search <terms>|inventory');
  process.exitCode = 1;
}
