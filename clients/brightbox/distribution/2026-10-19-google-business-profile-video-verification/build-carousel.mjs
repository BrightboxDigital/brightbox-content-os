#!/usr/bin/env node

import fs from "node:fs";
import path from "node:path";
import { spawnSync } from "node:child_process";
import { fileURLToPath } from "node:url";

const here = path.dirname(fileURLToPath(import.meta.url));
const repo = path.resolve(here, "../../../..");
const assets = path.join(repo, "clients/brightbox/approved/BBX-006-images");

const proofGraphic = dataUri(path.join(assets, "gbp-video-verification-three-part-checklist.png"));
const routeGraphic = dataUri(path.join(assets, "service-business-video-verification-recording-route.png"));

const sets = [
  {
    name: "instagram-linkedin-1080x1350",
    width: 1080,
    height: 1350,
    prefix: "ig",
  },
  {
    name: "facebook-1080x1080",
    width: 1080,
    height: 1080,
    prefix: "fb",
  },
];

for (const set of sets) {
  const outDir = path.join(here, "carousel-slides", set.name);
  fs.mkdirSync(outDir, { recursive: true });
  const slides = buildSlides(set.width, set.height);
  slides.forEach((svg, index) => {
    const out = path.join(outDir, `${set.prefix}_s${index + 1}.png`);
    rasterize(svg, out);
  });
}

const pinterestDir = path.join(here, "carousel-slides", "pinterest-1000x1500");
fs.mkdirSync(pinterestDir, { recursive: true });
rasterize(buildSlides(1000, 1500)[0], path.join(pinterestDir, "pinterest-cover.png"));

const portrait = Array.from({ length: 6 }, (_, i) =>
  path.join(here, "carousel-slides", "instagram-linkedin-1080x1350", `ig_s${i + 1}.png`),
);
const preview = path.join(here, "carousel-preview.jpg");
const montage = spawnSync(
  "magick",
  ["montage", "-font", "/System/Library/Fonts/Supplemental/Arial.ttf", ...portrait, "-tile", "3x2", "-geometry", "360x450+18+18", "-background", "#eef2f8", preview],
  { encoding: "utf8" },
);
if (montage.status !== 0) {
  throw new Error(montage.stderr || "Unable to create carousel preview");
}

console.log(`Built 13 carousel images and preview: ${preview}`);

function buildSlides(width, height) {
  return [
    coverSlide(width, height),
    graphicSlide(
      width,
      height,
      "THE THREE-PART TEST",
      ["Google wants three", "kinds of proof"],
      proofGraphic,
      "Location. Operations. Management.",
      "Make each one easy to see in one continuous recording.",
    ),
    graphicSlide(
      width,
      height,
      "PLAN BEFORE YOU RECORD",
      ["Use one clear", "recording route"],
      routeGraphic,
      "Marker → workspace → tools → access",
      "Walk the route once before you tap record.",
    ),
    checklistSlide(
      width,
      height,
      "MAKE IT EASY TO REVIEW",
      ["Keep the video", "short and clear"],
      [
        ["Show the requested proof first", "Do not make the reviewer hunt for it."],
        ["Record one continuous take", "Avoid cuts, edits, or a long improvised tour."],
        ["Add extra proof when it helps", "Signs, paperwork, branded materials, and equipment can support the case."],
        ["Protect private information", "Show what is needed without exposing sensitive details."],
      ],
    ),
    checklistSlide(
      width,
      height,
      "IF THE VIDEO IS REJECTED",
      ["Fix the missing proof", "and try again"],
      [
        ["Read the issue Google reports", "Start with the reason shown in the verification flow."],
        ["Re-record that proof clearly", "Make the missing evidence obvious and quick to understand."],
        ["Retry through the available path", "A rejection does not always mean the evidence was wrong."],
        ["Contact support after failures", "Ask for a human review when the normal process keeps failing."],
      ],
      "No checklist guarantees approval.",
    ),
    closingSlide(width, height),
  ];
}

function coverSlide(width, height) {
  const square = height === width;
  const headlineY = square ? 520 : 690;
  const font = square ? 70 : 76;
  const lineGap = square ? 80 : 88;
  return svgDoc(
    width,
    height,
    `
      ${baseBackground(width, height)}
      ${topRule(width)}
      ${eyebrow("GOOGLE BUSINESS PROFILE", 78, square ? 130 : 150, 25)}
      ${multiLine(["Before you record", "your verification", "video"], 78, headlineY, font, lineGap, "white", 760)}
      <text x="78" y="${headlineY + lineGap * 3 + 30}" class="body" font-size="34" fill="#E4EBF7">A practical checklist for service businesses</text>
      <text x="78" y="${headlineY + lineGap * 3 + 98}" class="heading" font-size="22" fill="#FFC163">LOCATION  •  OPERATIONS  •  MANAGEMENT</text>
      ${footer(width, height, "SAVE THIS BEFORE YOU RECORD")}
    `,
  );
}

function graphicSlide(width, height, label, titleLines, image, takeaway, note) {
  const square = height === width;
  const titleY = square ? 185 : 205;
  const frameY = square ? 330 : 400;
  const frameH = square ? 465 : 520;
  const bottomY = frameY + frameH + (square ? 70 : 88);
  return svgDoc(
    width,
    height,
    `
      ${baseBackground(width, height)}
      ${topRule(width)}
      ${eyebrow(label, 78, 120, 24)}
      ${multiLine(titleLines, 78, titleY, square ? 58 : 64, square ? 66 : 72, "white", 920)}
      <rect x="64" y="${frameY - 18}" width="${width - 128}" height="${frameH + 36}" rx="28" fill="#FFFFFF" opacity="0.98"/>
      <image href="${image}" x="82" y="${frameY}" width="${width - 164}" height="${frameH}" preserveAspectRatio="xMidYMid meet"/>
      <text x="${width / 2}" y="${bottomY}" text-anchor="middle" class="heading" font-size="${square ? 37 : 42}" fill="#FFC163">${escapeXml(takeaway)}</text>
      <text x="${width / 2}" y="${bottomY + 56}" text-anchor="middle" class="body" font-size="${square ? 25 : 28}" fill="#DDE5F3">${escapeXml(note)}</text>
      ${footer(width, height, "SWIPE FOR THE NEXT STEP")}
    `,
  );
}

function checklistSlide(width, height, label, titleLines, items, closing = "") {
  const square = height === width;
  const titleY = square ? 180 : 205;
  const startY = square ? 350 : 395;
  const gap = square ? 150 : 180;
  const titleSize = square ? 42 : 46;
  const bodySize = square ? 24 : 27;
  const blocks = items
    .map(([title, body], index) => {
      const y = startY + index * gap;
      return `
        <circle cx="108" cy="${y - 10}" r="30" fill="#FFC163"/>
        <path d="M94 ${y - 10} l9 10 l19 -24" fill="none" stroke="#0A1530" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>
        <text x="164" y="${y}" class="heading" font-size="${titleSize}" fill="white">${escapeXml(title)}</text>
        ${wrappedText(body, 164, y + 47, bodySize, width - 235, "#D9E2F2", 1.28)}
      `;
    })
    .join("");
  return svgDoc(
    width,
    height,
    `
      ${baseBackground(width, height)}
      ${topRule(width)}
      ${eyebrow(label, 78, 120, 24)}
      ${multiLine(titleLines, 78, titleY, square ? 58 : 64, square ? 66 : 72, "white", 920)}
      ${blocks}
      ${closing ? `<text x="${width / 2}" y="${height - 120}" text-anchor="middle" class="body" font-size="27" fill="#FFC163">${escapeXml(closing)}</text>` : ""}
      ${footer(width, height, closing ? "KEEP THE PROCESS MOVING" : "CLARITY BEATS A LONG TOUR")}
    `,
  );
}

function closingSlide(width, height) {
  const square = height === width;
  const headlineY = square ? 500 : 660;
  const font = square ? 66 : 72;
  const gap = square ? 76 : 84;
  return svgDoc(
    width,
    height,
    `
      ${baseBackground(width, height)}
      ${topRule(width)}
      ${eyebrow("FULL SERVICE-BUSINESS CHECKLIST", 78, square ? 130 : 150, 24)}
      ${multiLine(["Use the checklist", "before you record", "again"], 78, headlineY, font, gap, "white", 760)}
      <text x="78" y="${headlineY + gap * 3 + 30}" class="body" font-size="31" fill="#E4EBF7">Evidence examples • one-take route • rejection steps</text>
      <text x="78" y="${headlineY + gap * 3 + 92}" class="heading" font-size="38" fill="#FFC163">Read the full guide</text>
      ${footer(width, height, "BRIGHTBOXDIGITAL.IO/BLOG")}
    `,
  );
}

function svgDoc(width, height, body) {
  return `<?xml version="1.0" encoding="UTF-8"?>
  <svg xmlns="http://www.w3.org/2000/svg" width="${width}" height="${height}" viewBox="0 0 ${width} ${height}">
    <style>
      .heading { font-family: Arial, Helvetica, sans-serif; font-weight: 700; }
      .body { font-family: Arial, Helvetica, sans-serif; font-weight: 400; }
      .eyebrow { font-family: Arial, Helvetica, sans-serif; font-weight: 700; letter-spacing: 5px; }
    </style>
    ${body}
  </svg>`;
}

function baseBackground(width, height) {
  return `
    <rect width="${width}" height="${height}" fill="#10275E"/>
    <circle cx="${width + 40}" cy="40" r="290" fill="#6E36B5" opacity="0.62"/>
    <circle cx="-30" cy="${height - 40}" r="240" fill="#0E4C83" opacity="0.66"/>
  `;
}

function topRule(width) {
  return `<rect x="78" y="70" width="${width - 156}" height="10" rx="5" fill="#FFC163"/>`;
}

function eyebrow(text, x, y, size) {
  return `<text x="${x}" y="${y}" class="eyebrow" font-size="${size}" fill="#FFC163">${escapeXml(text)}</text>`;
}

function multiLine(lines, x, y, size, gap, fill, maxWidth) {
  return lines
    .map(
      (line, index) =>
        `<text x="${x}" y="${y + index * gap}" class="heading" font-size="${size}" fill="${fill}" textLength="${Math.min(maxWidth, line.length * size * 0.58)}" lengthAdjust="spacingAndGlyphs">${escapeXml(line)}</text>`,
    )
    .join("");
}

function wrappedText(text, x, y, size, maxWidth, fill, lineHeight) {
  const words = text.split(/\s+/);
  const lines = [];
  let current = "";
  const maxChars = Math.max(18, Math.floor(maxWidth / (size * 0.54)));
  for (const word of words) {
    const candidate = current ? `${current} ${word}` : word;
    if (candidate.length > maxChars && current) {
      lines.push(current);
      current = word;
    } else {
      current = candidate;
    }
  }
  if (current) lines.push(current);
  return `<text x="${x}" y="${y}" class="body" font-size="${size}" fill="${fill}">${lines
    .map((line, index) => `<tspan x="${x}" dy="${index === 0 ? 0 : size * lineHeight}">${escapeXml(line)}</tspan>`)
    .join("")}</text>`;
}

function footer(width, height, text) {
  return `
    <line x1="78" y1="${height - 74}" x2="${width - 78}" y2="${height - 74}" stroke="#FFFFFF" stroke-opacity="0.24" stroke-width="2"/>
    <text x="78" y="${height - 34}" class="eyebrow" font-size="18" fill="#FFFFFF" opacity="0.82">${escapeXml(text)}</text>
  `;
}

function rasterize(svg, output) {
  const result = spawnSync(
    "magick",
    ["-font", "/System/Library/Fonts/Supplemental/Arial.ttf", "svg:-", "-strip", "-quality", "92", output],
    {
    input: svg,
    encoding: "utf8",
    maxBuffer: 20 * 1024 * 1024,
    },
  );
  if (result.status !== 0) {
    throw new Error(result.stderr || `Unable to render ${output}`);
  }
}

function dataUri(file) {
  return file;
}

function escapeXml(value) {
  return value.replaceAll("&", "&amp;").replaceAll("<", "&lt;").replaceAll(">", "&gt;");
}
