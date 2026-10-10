#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EmCAD Complete Master Handbook & PDF Builder
Generates:
1. EmCAD_Interactive_Handbook.html
2. EmCAD_Complete_Master_Guide_Book.pdf
"""

import os
import sys
import subprocess

WORKSPACE = '/Users/manavramani/Desktop/emCad_explain_software'
ASSET_DIR = os.path.join(WORKSPACE, 'emCad_organized_assets')
HTML_OUTPUT = os.path.join(WORKSPACE, 'EmCAD_Interactive_Handbook.html')
PDF_OUTPUT = os.path.join(WORKSPACE, 'EmCAD_Complete_Master_Guide_Book.pdf')
CHROME_BIN = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'


def comparison_card(filename, title, subtitle, desc_items):
    rel_path = f"emCad_organized_assets/{filename}"
    items_html = "".join([f"<li>{item}</li>" for item in desc_items])
    return f"""
    <div class="comparison-card">
        <div class="comparison-header">
            <div class="comparison-badge">⚡ Vector vs Real Stitched Fabric Comparison</div>
            <h4>{title}</h4>
            <p class="comparison-subtitle">{subtitle}</p>
        </div>
        <div class="comparison-image-container" onclick="openModal('{rel_path}', '{title}')">
            <img src="{rel_path}" alt="{title}" loading="lazy">
        </div>
        <div class="comparison-details">
            <div class="anatomy-heading">🔍 કિસકો ક્યા કહા જાતા હૈ (Anatomy & Parts Terminology):</div>
            <ul class="anatomy-list">
                {items_html}
            </ul>
        </div>
    </div>"""

def drv_img_card(filename, title, desc):
    rel_path = f"emCad_organized_assets/drive_reference_gallery/{filename}"
    return f"""
    <div class="image-card">
        <div class="image-container" onclick="openModal('{rel_path}', '{title}')">
            <img src="{rel_path}" alt="{title}" loading="lazy">
        </div>
        <div class="image-caption">
            <strong>{title}</strong>
            <span>{desc}</span>
        </div>
    </div>"""

def img_card(filename, title, desc):
    rel_path = f"emCad_organized_assets/{filename}"
    return f"""
    <div class="image-card">
        <div class="image-container" onclick="openModal('{rel_path}', '{title}')">
            <img src="{rel_path}" alt="{title}" loading="lazy">
        </div>
        <div class="image-caption">
            <strong>{title}</strong>
            <span>{desc}</span>
        </div>
    </div>"""

HTML_HEAD = """<!DOCTYPE html>
<html lang="gu">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>EmCAD Embroidery Software - Complete Master Guide Book</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Noto+Sans+Gujarati:wght@400;500;600;700&family=Fira+Code:wght@400;600&display=swap" rel="stylesheet">
    <style>
        :root {
            --primary: #0F294A;
            --primary-dark: #07172C;
            --secondary: #1E6091;
            --accent: #D97706;
            --accent-light: #FEF3C7;
            --success: #059669;
            --success-light: #ECFDF5;
            --danger: #DC2626;
            --danger-light: #FEF2F2;
            --bg: #F8FAFC;
            --card-bg: #FFFFFF;
            --text-main: #1E293B;
            --text-muted: #64748B;
            --border: #E2E8F0;
            --shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.07), 0 2px 4px -2px rgba(0, 0, 0, 0.05);
            --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.08), 0 4px 6px -4px rgba(0, 0, 0, 0.04);
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: 'Inter', 'Noto Sans Gujarati', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background-color: var(--bg);
            color: var(--text-main);
            line-height: 1.6;
            font-size: 14px;
        }

        /* Top Header Navbar */
        .top-nav {
            position: sticky;
            top: 0;
            z-index: 100;
            background: rgba(15, 41, 74, 0.95);
            backdrop-filter: blur(10px);
            color: #FFFFFF;
            padding: 12px 24px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        }

        .nav-brand {
            display: flex;
            align-items: center;
            gap: 12px;
            font-weight: 700;
            font-size: 16px;
            letter-spacing: 0.5px;
        }

        .nav-brand span {
            background: linear-gradient(135deg, #F59E0B, #D97706);
            padding: 4px 8px;
            border-radius: 4px;
            font-size: 12px;
            color: #000;
            font-weight: 800;
        }

        .search-container {
            display: flex;
            align-items: center;
            gap: 10px;
            max-width: 420px;
            width: 100%;
        }

        .search-box {
            width: 100%;
            padding: 8px 14px;
            border-radius: 20px;
            border: 1px solid rgba(255,255,255,0.25);
            background: rgba(255,255,255,0.1);
            color: #FFFFFF;
            font-size: 13px;
            outline: none;
            transition: all 0.2s;
        }

        .search-box:focus {
            background: rgba(255,255,255,0.2);
            border-color: #F59E0B;
        }

        .search-box::placeholder {
            color: rgba(255,255,255,0.6);
        }

        .print-btn {
            background: #D97706;
            color: #FFFFFF;
            border: none;
            padding: 8px 16px;
            border-radius: 6px;
            font-weight: 600;
            font-size: 12px;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 6px;
            transition: background 0.2s;
        }

        .print-btn:hover {
            background: #B45309;
        }

        /* Container */
        .container {
            max-width: 1100px;
            margin: 24px auto;
            padding: 0 20px;
        }

        /* Cover Hero */
        .cover-hero {
            background: linear-gradient(135deg, #0F294A 0%, #1E3E62 60%, #0F294A 100%);
            border-radius: 12px;
            padding: 40px;
            color: #FFFFFF;
            margin-bottom: 30px;
            box-shadow: var(--shadow-lg);
            border-left: 6px solid #D97706;
        }

        .hero-badge {
            display: inline-block;
            background: rgba(217, 119, 6, 0.2);
            border: 1px solid #D97706;
            color: #FBBF24;
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 11px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 12px;
        }

        .cover-hero h1 {
            font-size: 28px;
            font-weight: 800;
            margin-bottom: 8px;
            line-height: 1.3;
        }

        .cover-hero h2 {
            font-size: 17px;
            font-weight: 500;
            color: #CBD5E1;
            margin-bottom: 20px;
        }

        .hero-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 16px;
            margin-top: 24px;
            padding-top: 20px;
            border-top: 1px solid rgba(255,255,255,0.15);
        }

        .hero-stat {
            background: rgba(255,255,255,0.06);
            padding: 12px 16px;
            border-radius: 8px;
            border: 1px solid rgba(255,255,255,0.1);
        }

        .hero-stat-num {
            font-size: 22px;
            font-weight: 800;
            color: #F59E0B;
        }

        .hero-stat-label {
            font-size: 12px;
            color: #CBD5E1;
            margin-top: 2px;
        }

        /* Navigation Pills */
        .nav-pills {
            display: flex;
            gap: 8px;
            flex-wrap: wrap;
            margin-bottom: 24px;
            background: #FFFFFF;
            padding: 12px;
            border-radius: 10px;
            box-shadow: var(--shadow);
            border: 1px solid var(--border);
        }

        .nav-pill {
            padding: 6px 14px;
            border-radius: 6px;
            font-size: 12px;
            font-weight: 600;
            color: var(--text-main);
            text-decoration: none;
            background: #F1F5F9;
            transition: all 0.2s;
            display: inline-flex;
            align-items: center;
            gap: 4px;
        }

        .nav-pill:hover, .nav-pill.active {
            background: var(--primary);
            color: #FFFFFF;
        }

        
        /* Side-by-Side Comparison Cards */
        .comparison-card {
            background: #FFFFFF;
            border: 2px solid #0F294A;
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 10px 25px -5px rgba(15, 41, 74, 0.12), 0 8px 10px -6px rgba(15, 41, 74, 0.08);
            margin: 28px 0;
            transition: transform 0.2s, box-shadow 0.2s;
        }

        .comparison-card:hover {
            box-shadow: 0 20px 30px -10px rgba(15, 41, 74, 0.2);
        }

        .comparison-header {
            background: linear-gradient(135deg, #0F294A 0%, #1E3A8A 100%);
            color: #FFFFFF;
            padding: 16px 22px;
        }

        .comparison-badge {
            display: inline-block;
            background: #D97706;
            color: #FFFFFF;
            font-size: 11px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.8px;
            padding: 3px 12px;
            border-radius: 12px;
            margin-bottom: 8px;
        }

        .comparison-header h4 {
            font-size: 18px;
            font-weight: 700;
            margin-bottom: 4px;
            color: #FFFFFF;
        }

        .comparison-subtitle {
            font-size: 13px;
            color: #CBD5E1;
            line-height: 1.4;
        }

        .comparison-image-container {
            width: 100%;
            background: #07172C;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 12px;
            cursor: pointer;
        }

        .comparison-image-container img {
            width: 100%;
            max-height: 650px;
            object-fit: contain;
            border-radius: 6px;
            display: block;
        }

        .comparison-details {
            background: #F8FAFC;
            padding: 20px 24px;
            border-top: 1px solid #E2E8F0;
        }

        .anatomy-heading {
            font-size: 14.5px;
            font-weight: 700;
            color: #0F294A;
            margin-bottom: 12px;
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .anatomy-list {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
            gap: 12px 20px;
            list-style: none;
            padding: 0;
            margin: 0;
        }

        .anatomy-list li {
            position: relative;
            padding-left: 20px;
            font-size: 12.5px;
            line-height: 1.55;
            color: #334155;
        }

        .anatomy-list li::before {
            content: "▸";
            position: absolute;
            left: 0;
            color: #D97706;
            font-weight: bold;
            font-size: 14px;
        }

        .anatomy-list li b {
            color: #0F294A;
        }

        
        /* Enhanced Interactive Embroidery Studio & Simulator */
        .sim-container {
            background: radial-gradient(circle at top, #112240 0%, #07111E 100%);
            border: 2px solid #233554;
            border-radius: 14px;
            padding: 22px;
            margin: 24px 0;
            color: #FFFFFF;
            box-shadow: 0 16px 40px rgba(0,0,0,0.5), inset 0 1px 0 rgba(255,255,255,0.1);
        }

        .sim-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 16px;
            padding-bottom: 12px;
            border-bottom: 1px solid #1E2D4A;
        }

        .sim-header h3 {
            margin: 0;
            font-size: 18px;
            color: #F8FAFC;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .sim-header .sim-badge {
            background: #0D2847;
            color: #38BDF8;
            border: 1px solid #0284C7;
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: 700;
            letter-spacing: 0.5px;
        }

        .sim-controls {
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
            align-items: center;
            margin-bottom: 14px;
            background: rgba(15, 23, 42, 0.7);
            padding: 12px 16px;
            border-radius: 10px;
            border: 1px solid #1E293B;
        }

        .sim-btn {
            background: linear-gradient(135deg, #D97706, #B45309);
            color: #FFFFFF;
            border: none;
            padding: 8px 16px;
            border-radius: 6px;
            font-weight: 700;
            font-size: 13px;
            cursor: pointer;
            transition: all 0.2s;
            display: inline-flex;
            align-items: center;
            gap: 6px;
            box-shadow: 0 2px 6px rgba(217, 119, 6, 0.4);
        }

        .sim-btn:hover {
            background: linear-gradient(135deg, #F59E0B, #D97706);
            transform: translateY(-1px);
        }

        .sim-btn-secondary {
            background: #1E293B;
            border: 1px solid #334155;
            box-shadow: none;
        }

        .sim-btn-secondary:hover {
            background: #334155;
            border-color: #64748B;
        }

        .sim-select {
            padding: 8px 14px;
            border-radius: 6px;
            background: #0F172A;
            color: #F8FAFC;
            border: 1px solid #334155;
            font-size: 13px;
            font-weight: 600;
            outline: none;
            cursor: pointer;
        }

        .sim-select:focus {
            border-color: #38BDF8;
        }

        .sim-scrubber-box {
            display: flex;
            align-items: center;
            gap: 12px;
            margin-bottom: 14px;
            background: rgba(15, 23, 42, 0.5);
            padding: 8px 16px;
            border-radius: 8px;
            border: 1px solid #1E293B;
        }

        .sim-scrubber-box label {
            font-size: 12px;
            font-weight: 600;
            color: #94A3B8;
            white-space: nowrap;
        }

        .sim-scrubber {
            flex: 1;
            height: 6px;
            border-radius: 3px;
            background: #334155;
            outline: none;
            accent-color: #F59E0B;
            cursor: pointer;
        }

        .sim-canvas-wrapper {
            position: relative;
            border-radius: 10px;
            overflow: hidden;
            border: 2px solid #1E2D4A;
            box-shadow: inset 0 0 30px rgba(0,0,0,0.8);
        }

        .sim-canvas {
            width: 100%;
            height: 420px;
            background: #0B1424;
            display: block;
        }

        .sim-telemetry-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(170px, 1fr));
            gap: 10px;
            margin-top: 14px;
        }

        .sim-hud-card {
            background: rgba(15, 23, 42, 0.85);
            border: 1px solid #1E293B;
            border-radius: 8px;
            padding: 8px 12px;
        }

        .sim-hud-label {
            font-size: 10.5px;
            color: #94A3B8;
            font-family: 'Fira Code', monospace;
            text-transform: uppercase;
            margin-bottom: 4px;
        }

        .sim-hud-val {
            font-size: 13.5px;
            font-weight: 700;
            font-family: 'Fira Code', monospace;
            color: #38BDF8;
        }

        /* GIF Animation Cards */
        .anim-card {
            background: #FFFFFF;
            border: 1px solid #CBD5E1;
            border-radius: 10px;
            overflow: hidden;
            box-shadow: var(--shadow);
            margin: 20px 0;
        }

        .anim-card-header {
            background: #0F294A;
            color: #FFFFFF;
            padding: 12px 18px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .anim-card-header h4 {
            font-size: 15px;
            margin: 0;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .anim-container {
            width: 100%;
            background: #07172C;
            display: flex;
            justify-content: center;
            padding: 8px;
        }

        .anim-container img {
            max-width: 100%;
            max-height: 480px;
            border-radius: 4px;
            display: block;
        }

        .anim-caption {
            padding: 14px 18px;
            background: #F8FAFC;
            font-size: 13px;
            border-top: 1px solid #E2E8F0;
            line-height: 1.5;
        }

        /* Quiz Styles */
        .quiz-card {
            background: #FFFFFF;
            border: 2px solid #E2E8F0;
            border-radius: 10px;
            padding: 20px;
            margin: 16px 0;
            transition: all 0.2s;
        }

        .quiz-card:hover {
            border-color: #3B82F6;
        }

        .quiz-q {
            font-size: 15px;
            font-weight: 700;
            color: #0F294A;
            margin-bottom: 14px;
        }

        .quiz-options {
            display: flex;
            flex-direction: column;
            gap: 8px;
        }

        .quiz-option {
            background: #F8FAFC;
            border: 1px solid #CBD5E1;
            padding: 10px 14px;
            border-radius: 6px;
            cursor: pointer;
            font-size: 13.5px;
            transition: all 0.2s;
        }

        .quiz-option:hover {
            background: #EFF6FF;
            border-color: #3B82F6;
        }

        .quiz-option.correct {
            background: #ECFDF5 !important;
            border-color: #059669 !important;
            color: #065F46 !important;
            font-weight: 700;
        }

        .quiz-option.wrong {
            background: #FEF2F2 !important;
            border-color: #DC2626 !important;
            color: #991B1B !important;
            font-weight: 700;
        }

        .quiz-feedback {
            margin-top: 10px;
            padding: 8px 12px;
            border-radius: 6px;
            font-size: 12.5px;
            display: none;
        }

        /* Project Step Cards */
        .project-step {
            border-left: 3px solid #D97706;
            padding-left: 16px;
            margin: 16px 0;
        }

        .project-step-title {
            font-size: 14.5px;
            font-weight: 700;
            color: #0F294A;
            margin-bottom: 4px;
        }

        /* Section Cards */
        .section-card {
            background: var(--card-bg);
            border-radius: 12px;
            padding: 30px;
            margin-bottom: 30px;
            box-shadow: var(--shadow);
            border: 1px solid var(--border);
        }

        .section-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding-bottom: 16px;
            margin-bottom: 20px;
            border-bottom: 2px solid var(--border);
        }

        .section-title {
            display: flex;
            align-items: center;
            gap: 12px;
            font-size: 20px;
            font-weight: 700;
            color: var(--primary);
        }

        .section-tag {
            background: #EEF2F6;
            color: var(--secondary);
            font-size: 11px;
            padding: 4px 10px;
            border-radius: 12px;
            font-weight: 600;
        }

        /* Tables */
        .data-table {
            width: 100%;
            border-collapse: collapse;
            margin: 16px 0;
            font-size: 12.5px;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        }

        .data-table th {
            background: var(--primary);
            color: #FFFFFF;
            font-weight: 600;
            padding: 10px 14px;
            text-align: left;
            font-size: 12px;
            letter-spacing: 0.3px;
        }

        .data-table td {
            padding: 10px 14px;
            border-bottom: 1px solid var(--border);
            vertical-align: top;
        }

        .data-table tr:nth-child(even) td {
            background-color: #F8FAFC;
        }

        .data-table tr:hover td {
            background-color: #F1F5F9;
        }

        .badge-code {
            font-family: 'Fira Code', monospace;
            background: #E2E8F0;
            color: #0F172A;
            padding: 2px 6px;
            border-radius: 4px;
            font-size: 11px;
            font-weight: 600;
            white-space: nowrap;
        }

        .badge-num {
            background: var(--secondary);
            color: #FFFFFF;
            padding: 2px 6px;
            border-radius: 4px;
            font-size: 11px;
            font-weight: 700;
            display: inline-block;
            text-align: center;
            min-width: 24px;
        }

        /* Callout / Alert Box */
        .callout {
            border-radius: 8px;
            padding: 16px 20px;
            margin: 16px 0;
            display: flex;
            gap: 14px;
            align-items: flex-start;
            border-left: 4px solid;
            font-size: 13px;
        }

        .callout-tip {
            background-color: var(--success-light);
            border-color: var(--success);
            color: #064E3B;
        }

        .callout-warning {
            background-color: var(--accent-light);
            border-color: var(--accent);
            color: #78350F;
        }

        .callout-danger {
            background-color: var(--danger-light);
            border-color: var(--danger);
            color: #7F1D1D;
        }

        .callout-icon {
            font-size: 20px;
            line-height: 1;
        }

        .callout-content strong {
            display: block;
            margin-bottom: 4px;
            font-size: 13.5px;
        }

        /* Image Display Grid & Figure */
        .image-gallery {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
            gap: 20px;
            margin: 20px 0;
        }

        
            .comparison-card {
                page-break-inside: avoid;
                margin-bottom: 15mm;
                border: 1px solid #0F294A;
                box-shadow: none;
                -webkit-print-color-adjust: exact;
                print-color-adjust: exact;
            }
            .comparison-image-container img {
                max-height: 520px;
            }

            .image-card {
            background: #FFFFFF;
            border: 1px solid var(--border);
            border-radius: 8px;
            overflow: hidden;
            box-shadow: var(--shadow);
            transition: transform 0.2s, box-shadow 0.2s;
            display: flex;
            flex-direction: column;
        }

        .image-card:hover {
            transform: translateY(-2px);
            box-shadow: var(--shadow-lg);
        }

        .image-container {
            width: 100%;
            background: #0F172A;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 8px;
            cursor: pointer;
            max-height: 440px;
            overflow: hidden;
        }

        .image-container img {
            max-width: 100%;
            max-height: 420px;
            object-fit: contain;
            border-radius: 4px;
            display: block;
        }

        .image-caption {
            padding: 12px 16px;
            background: #FFFFFF;
            font-size: 12px;
            color: var(--text-main);
            border-top: 1px solid var(--border);
            flex-grow: 1;
        }

        .image-caption strong {
            color: var(--primary);
            display: block;
            margin-bottom: 2px;
            font-size: 12.5px;
        }

        /* Lightbox Modal */
        .modal {
            display: none;
            position: fixed;
            z-index: 1000;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0,0,0,0.9);
            justify-content: center;
            align-items: center;
            flex-direction: column;
            padding: 20px;
        }

        .modal.active {
            display: flex;
        }

        .modal img {
            max-width: 90vw;
            max-height: 85vh;
            object-fit: contain;
            border-radius: 6px;
            box-shadow: 0 0 25px rgba(255,255,255,0.2);
        }

        .modal-caption {
            color: #FFFFFF;
            margin-top: 12px;
            font-size: 14px;
            text-align: center;
            max-width: 800px;
        }

        .modal-close {
            position: absolute;
            top: 20px;
            right: 25px;
            color: #FFFFFF;
            font-size: 32px;
            font-weight: 700;
            cursor: pointer;
        }

        /* Footer */
        .master-footer {
            background: var(--primary-dark);
            color: #CBD5E1;
            padding: 30px 20px;
            text-align: center;
            font-size: 12px;
            margin-top: 40px;
            border-top: 3px solid #D97706;
        }

        /* Print Specific Styling */
        @media print {
            @page {
                size: A4 portrait;
                margin: 10mm 12mm 12mm 12mm;
            }

            body {
                background: #FFFFFF;
                color: #000000;
                font-size: 10pt;
            }

            .top-nav, .nav-pills, .print-btn, .search-container, .modal {
                display: none !important;
            }

            .container {
                max-width: 100%;
                margin: 0;
                padding: 0;
            }

            .cover-hero {
                page-break-after: always;
                border-radius: 0;
                padding: 25mm 15mm;
                margin-bottom: 0;
                box-shadow: none;
                background: #0F294A !important;
                -webkit-print-color-adjust: exact;
                print-color-adjust: exact;
            }

            .section-card {
                page-break-before: always;
                border: none;
                box-shadow: none;
                padding: 0;
                margin: 0 0 15mm 0;
            }

            .data-table {
                box-shadow: none;
                page-break-inside: auto;
            }

            .data-table tr {
                page-break-inside: avoid;
                page-break-after: auto;
            }

            .data-table th {
                background-color: #0F294A !important;
                color: #FFFFFF !important;
                -webkit-print-color-adjust: exact;
                print-color-adjust: exact;
            }

            .data-table tr:nth-child(even) td {
                background-color: #F8FAFC !important;
                -webkit-print-color-adjust: exact;
                print-color-adjust: exact;
            }

            .callout {
                page-break-inside: avoid;
                -webkit-print-color-adjust: exact;
                print-color-adjust: exact;
            }

            .image-gallery {
                display: block;
            }

            
            .comparison-card {
                page-break-inside: avoid;
                margin-bottom: 15mm;
                border: 1px solid #0F294A;
                box-shadow: none;
                -webkit-print-color-adjust: exact;
                print-color-adjust: exact;
            }
            .comparison-image-container img {
                max-height: 520px;
            }

            .image-card {
                page-break-inside: avoid;
                margin-bottom: 10mm;
                border: 1px solid #CBD5E1;
                box-shadow: none;
            }

            .image-container {
                background: transparent;
                padding: 0;
            }

            .image-container img {
                max-height: 440px;
                width: auto;
                margin: 0 auto;
            }
        }
    </style>
</head>
<body>

    <!-- TOP NAVIGATION -->
    <nav class="top-nav">
        <div class="nav-brand">
            🧵 EmCAD Master Guide <span>2026 EDITION</span>
        </div>
        <div class="search-container">
            <input type="text" id="searchInput" class="search-box" placeholder="શોધો (Search): ટૂલ, સ્ટેપ, શોર્ટકટ, બીડ્સ, સિક્વિન...">
        </div>
        <button class="print-btn" onclick="window.print()">
            🖨️ Print / Save as PDF
        </button>
    </nav>

    <div class="container">

        <!-- COVER HERO -->
        <div class="cover-hero">
            <span class="hero-badge">OFFICIAL PUNCHING & PRODUCTION MANUAL</span>
            <h1>EmCAD એમ્બ્રોઇડરી ડિઝાઇન સોફ્ટવેર</h1>
            <h2>સંપૂર્ણ માસ્ટર ગાઇડ બુક: ટૂલ્સ ૧ થી ૫૨, સ્ટેપ ૧ થી ૧૬, સિક્વિન, બીડ્સ, કોર્ડિંગ અને દહાઓ મશીન સેટિંગ્સ</h2>
            <p style="font-size: 13.5px; color: #E2E8F0; max-width: 900px; margin-top: 10px;">
                આ ગાઇડ તમારી મૂળ રેફરન્સ બુક, પ્રેક્ટિકલ અનુભવ અને ઓરિજિનલ વર્કશોપ નોટ્સના આધારે તૈયાર કરવામાં આવી છે.
                અહીં તમામ 52 ટૂલ્સ, 16 સ્ટેપ્સ, કીબોર્ડ શોર્ટકટ્સ, દહાઓ મશીન પેરામીટર્સ, બીડ્સ ટાંકા ગણતરી અને ૨૫-હેડ મલ્ટી-હેડ પ્રોડક્શન નિયમોને
                સરળ ગુજરાતી અને હિંગ્લિશમાં સચિત્ર સમજાવવામાં આવ્યા છે.
            </p>

            <div class="hero-grid">
                <div class="hero-stat">
                    <div class="hero-stat-num">૫૨ ટૂલ્સ</div>
                    <div class="hero-stat-label">તમામ સિમ્બોલ્સ & શોર્ટકટ્સ</div>
                </div>
                <div class="hero-stat">
                    <div class="hero-stat-num">૧૬ સ્ટેપ્સ</div>
                    <div class="hero-stat-label">ડ્રોઇંગથી ફાઇનલ પ્રોડક્શન</div>
                </div>
                <div class="hero-stat">
                    <div class="hero-stat-num">૧૧૧ ચિત્રો</div>
                    <div class="hero-stat-label">૭૪ HD અપસ્કેલ + ૩૭ ડ્રાઇવ રેફરન્સ સ્વેચીસ</div>
                </div>
                <div class="hero-stat">
                    <div class="hero-stat-num">દહાઓ સેટિંગ્સ</div>
                    <div class="hero-stat-label">DHA, DHE, DST & 2/4 Beads</div>
                </div>
            </div>
        </div>

        <!-- NAVIGATION PILLS -->
        <div class="nav-pills">
            
            <a href="#sec-simulations" class="nav-pill" style="background:#0F294A; color:#F59E0B; border:1px solid #F59E0B;">🎬 Live Simulator</a>
            <a href="#sec-troubleshooting" class="nav-pill" style="background:#DC2626; color:#fff;">🛠️ Troubleshooting</a>
            <a href="#sec-projects" class="nav-pill" style="background:#059669; color:#fff;">🎯 3 Practical Projects</a>
            <a href="#sec-roadmap" class="nav-pill">🗓️ 7-Day Roadmap</a>
            <a href="#sec-slang" class="nav-pill">📖 Market Slang</a>
            <a href="#sec-dos-donts" class="nav-pill">⚖️ Do's & Don'ts</a>
            <a href="#sec-quiz" class="nav-pill" style="background:#8B5CF6; color:#fff;">🧠 Certification Quiz</a>

            <a href="#sec-comparisons" class="nav-pill" style="background:#D97706; color:#fff;">⚡ Vector vs Real Gallery</a>
            <a href="#sec-tools" class="nav-pill active">🛠️ Tools 1-52</a>
            <a href="#sec-units" class="nav-pill">📏 Units & Measurements</a>
            <a href="#sec-drawing" class="nav-pill">✏️ Step 1-2 Drawing</a>
            <a href="#sec-paghdi" class="nav-pill">👑 Step 3 Paghdi (F4)</a>
            <a href="#sec-punching" class="nav-pill">⚡ Step 4 Mechanics</a>
            <a href="#sec-fkeys" class="nav-pill">🎹 Step 5 F1-F12</a>
            <a href="#sec-repeats" class="nav-pill">📐 Step 6 & 12 Farma</a>
            <a href="#sec-motif" class="nav-pill">🌺 Step 7 Motif</a>
            <a href="#sec-density" class="nav-pill">✨ Step 8 Density</a>
            <a href="#sec-shading" class="nav-pill">🎨 Step 9 9-Needle & Shading</a>
            <a href="#sec-transform" class="nav-pill">🔄 Step 10 Transform</a>
            <a href="#sec-sequin-beads" class="nav-pill">📿 Sequin & Beads</a>
            <a href="#sec-looping-chenille" class="nav-pill" style="background:#4C1D95; color:#F5D0FE; border:1px solid #A855F7;">➰ Looping & Chenille</a>
            <a href="#sec-locks" class="nav-pill">🔒 Step 13 Locks</a>
            <a href="#sec-dahao" class="nav-pill">💾 Step 14 Dahao & Formats</a>
            <a href="#sec-saree" class="nav-pill">🥻 Step 15 Saree & 25-Head</a>
            <a href="#sec-finalize" class="nav-pill">🏁 Step 16 Finalize & Origin</a>
            <a href="#sec-shortcuts" class="nav-pill">⚡ Cheat Sheet</a>
        </div>
"""

HTML_FOOT = """
        <!-- MODAL LIGHTBOX -->
        <div class="modal" id="imageModal" onclick="closeModal()">
            <span class="modal-close">&times;</span>
            <img id="modalImg" src="" alt="Zoomed Image">
            <div class="modal-caption" id="modalCaption"></div>
        </div>

        <footer class="master-footer">
            <p><b>EmCAD Embroidery Design Software - Complete Master Guide Book</b></p>
            <p>તમામ હકો સુરક્ષિત © 2026 | Prepared for Professional Embroidery Punching Masters & Multi-Head Machine Operators</p>
        </footer>
    </div>

    <script>
        // Search functionality
        const searchInput = document.getElementById('searchInput');
        searchInput.addEventListener('input', function() {
            const query = this.value.toLowerCase().trim();
            const cards = document.querySelectorAll('.section-card');
            
            cards.forEach(card => {
                const text = card.innerText.toLowerCase();
                if (text.includes(query)) {
                    card.style.display = 'block';
                } else {
                    card.style.display = 'none';
                }
            });
        });

        // Modal Lightbox
        function openModal(src, caption) {
            const modal = document.getElementById('imageModal');
            const img = document.getElementById('modalImg');
            const cap = document.getElementById('modalCaption');
            img.src = src;
            cap.innerText = caption;
            modal.classList.add('active');
        }

        function closeModal() {
            document.getElementById('imageModal').classList.remove('active');
        }

        document.addEventListener('keydown', function(e) {
            if (e.key === 'Escape') closeModal();
        });

        // --- ADVANCED 3D EMBROIDERY STUDIO & SIMULATOR ---
        const simCanvas = document.getElementById('simCanvas');
        const ctx = simCanvas ? simCanvas.getContext('2d') : null;
        let simPlaying = false;
        let simTimer = null;
        let simFrame = 0;
        let simSpeed = 1;
        let soundEnabled = false;
        let audioCtx = null;
        let threadColor = '#EF4444';

        // Procedural Web Audio API Sound Synthesizer for Sewing Machine
        function playSewingSound(isTrim, isJump) {
            if (!soundEnabled) return;
            try {
                if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
                if (audioCtx.state === 'suspended') audioCtx.resume();
                const now = audioCtx.currentTime;
                const osc = audioCtx.createOscillator();
                const gain = audioCtx.createGain();
                osc.connect(gain);
                gain.connect(audioCtx.destination);

                if (isTrim) {
                    osc.type = 'sawtooth';
                    osc.frequency.setValueAtTime(900, now);
                    osc.frequency.exponentialRampToValueAtTime(140, now + 0.12);
                    gain.gain.setValueAtTime(0.25, now);
                    gain.gain.exponentialRampToValueAtTime(0.01, now + 0.12);
                    osc.start(now);
                    osc.stop(now + 0.12);
                } else if (isJump) {
                    osc.type = 'sine';
                    osc.frequency.setValueAtTime(320, now);
                    osc.frequency.exponentialRampToValueAtTime(120, now + 0.05);
                    gain.gain.setValueAtTime(0.03, now);
                    gain.gain.exponentialRampToValueAtTime(0.001, now + 0.05);
                    osc.start(now);
                    osc.stop(now + 0.05);
                } else {
                    // Crisp mechanical needle punch
                    osc.type = 'triangle';
                    osc.frequency.setValueAtTime(460, now);
                    osc.frequency.exponentialRampToValueAtTime(90, now + 0.04);
                    gain.gain.setValueAtTime(0.3, now);
                    gain.gain.exponentialRampToValueAtTime(0.005, now + 0.04);
                    osc.start(now);
                    osc.stop(now + 0.04);
                }
            } catch(e) {}
        }

        function toggleSound() {
            soundEnabled = !soundEnabled;
            const btn = document.getElementById('btnSound');
            if (btn) {
                btn.innerText = soundEnabled ? '🔊 Sound: ON' : '🔇 Sound: OFF';
                btn.style.borderColor = soundEnabled ? '#10B981' : '#334155';
            }
        }

        function onThreadColorChange(color) {
            threadColor = color;
            drawSimFrame();
        }

        function resetSim() {
            simPlaying = false;
            if (simTimer) clearInterval(simTimer);
            simFrame = 0;
            const btnPlay = document.getElementById('btnPlay');
            if (btnPlay) btnPlay.innerText = '▶ Play';
            const scrubber = document.getElementById('simScrubber');
            if (scrubber) scrubber.value = 0;
            drawSimFrame();
        }

        function togglePlaySim() {
            simPlaying = !simPlaying;
            const btnPlay = document.getElementById('btnPlay');
            if (simPlaying) {
                if (btnPlay) btnPlay.innerText = '⏸ Pause';
                simTimer = setInterval(tickSim, 50 / simSpeed);
            } else {
                if (btnPlay) btnPlay.innerText = '▶ Play';
                if (simTimer) clearInterval(simTimer);
            }
        }

        function stepSim(delta) {
            simPlaying = false;
            if (simTimer) clearInterval(simTimer);
            const btnPlay = document.getElementById('btnPlay');
            if (btnPlay) btnPlay.innerText = '▶ Play';
            simFrame = Math.max(0, Math.min(140, simFrame + delta));
            const scrubber = document.getElementById('simScrubber');
            if (scrubber) scrubber.value = simFrame;
            drawSimFrame();
        }

        function onScrubSim(val) {
            simFrame = parseInt(val);
            drawSimFrame();
        }

        function toggleSpeedSim() {
            const btnSpeed = document.getElementById('btnSpeed');
            if (simSpeed === 1) simSpeed = 2;
            else if (simSpeed === 2) simSpeed = 4;
            else if (simSpeed === 4) simSpeed = 8;
            else if (simSpeed === 8) simSpeed = 0.5;
            else simSpeed = 1;
            if (btnSpeed) btnSpeed.innerText = `⚡ Speed: ${simSpeed}x`;
            if (simPlaying) {
                clearInterval(simTimer);
                simTimer = setInterval(tickSim, 50 / simSpeed);
            }
        }

        function tickSim() {
            simFrame++;
            if (simFrame > 140) simFrame = 0;
            const scrubber = document.getElementById('simScrubber');
            if (scrubber) scrubber.value = simFrame;
            drawSimFrame();
        }

        function drawNeedleHead(ctx, nx, ny, isDown, strokeLen, threadCol) {
            // Spring & Presser foot ring
            const footY = isDown ? ny : ny - 10;
            ctx.strokeStyle = '#D97706';
            ctx.lineWidth = 2.5;
            ctx.beginPath();
            ctx.arc(nx, footY, 14, 0, Math.PI * 2);
            ctx.stroke();

            // Spring coils
            ctx.strokeStyle = '#64748B';
            ctx.lineWidth = 2;
            for (let c = 0; c < 3; c++) {
                const cy = footY - 14 - c * 8;
                ctx.beginPath();
                ctx.moveTo(nx - 7, cy);
                ctx.lineTo(nx + 7, cy + 4);
                ctx.stroke();
            }

            // Chrome needle bar
            const barTop = ny - 120;
            const grad = ctx.createLinearGradient(nx - 3, barTop, nx + 3, ny);
            grad.addColorStop(0, '#94A3B8');
            grad.addColorStop(0.5, '#F8FAFC');
            grad.addColorStop(1, '#475569');
            ctx.fillStyle = grad;
            ctx.fillRect(nx - 3, barTop, 6, 120);

            // Needle point tip
            ctx.fillStyle = '#CBD5E1';
            ctx.beginPath();
            ctx.moveTo(nx - 3, ny);
            ctx.lineTo(nx + 3, ny);
            ctx.lineTo(nx, ny + 12);
            ctx.fill();

            // Thread feed line through needle eye
            ctx.strokeStyle = threadCol;
            ctx.lineWidth = 2;
            ctx.beginPath();
            ctx.moveTo(nx + 8, barTop);
            ctx.lineTo(nx, ny + 6);
            ctx.lineTo(nx, ny + 12);
            ctx.stroke();

            // Cloth puncture hole shadow
            if (isDown) {
                ctx.fillStyle = 'rgba(0,0,0,0.6)';
                ctx.beginPath();
                ctx.arc(nx, ny + 12, 3, 0, Math.PI * 2);
                ctx.fill();
            }
        }

        function drawSimFrame() {
            if (!ctx) return;
            const w = simCanvas.width;
            const h = simCanvas.height;
            ctx.clearRect(0, 0, w, h);

            // 1. Woven fabric background (linen/silk weave pattern)
            ctx.fillStyle = '#081220';
            ctx.fillRect(0, 0, w, h);

            ctx.strokeStyle = '#0F1F38';
            ctx.lineWidth = 1;
            for (let x = 0; x < w; x += 18) {
                ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, h); ctx.stroke();
            }
            for (let y = 0; y < h; y += 18) {
                ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(w, y); ctx.stroke();
            }

            // Embroidery Hoop ring guideline
            ctx.strokeStyle = 'rgba(217, 119, 6, 0.2)';
            ctx.lineWidth = 4;
            ctx.beginPath();
            ctx.arc(w / 2, h / 2, Math.min(w, h) * 0.44, 0, Math.PI * 2);
            ctx.stroke();

            const scenario = document.getElementById('simScenario').value;
            const statusEl = document.getElementById('hudStatus');
            const coordsEl = document.getElementById('hudCoords');
            const countEl = document.getElementById('hudStitchCount');
            const rpmEl = document.getElementById('hudRpm');
            const strokeEl = document.getElementById('hudZStroke');

            let curX = 100, curY = 200;
            let status = 'READY';
            let isDown = true;
            let currentRpm = '850 RPM';
            let zStroke = 'DOWN (PIERCING)';

            // Enable 3D stitch drop-shadow
            ctx.shadowColor = 'rgba(0, 0, 0, 0.5)';
            ctx.shadowBlur = 4;
            ctx.shadowOffsetX = 1;
            ctx.shadowOffsetY = 2;

            if (scenario === 'jump') {
                // Scenario 1: Stitching vs Jump
                ctx.strokeStyle = '#38BDF8';
                ctx.lineWidth = 1.5;
                ctx.strokeRect(60, 110, 240, 190);
                ctx.strokeRect(580, 110, 240, 190);
                ctx.fillStyle = '#94A3B8';
                ctx.font = '12px Inter';
                ctx.fillText('Object 1 (Leaf - Red)', 70, 95);
                ctx.fillText('Object 2 (Flower - Green)', 590, 95);

                const maxStitches = Math.min(24, Math.floor(simFrame / 1.8));
                ctx.strokeStyle = threadColor;
                ctx.lineWidth = 3.5;
                for (let i = 0; i < maxStitches; i++) {
                    const sx = 80 + i * 9.5;
                    ctx.beginPath();
                    ctx.moveTo(sx, 130 + (i % 2) * 130);
                    ctx.lineTo(sx, 160 + (i % 2) * 130);
                    ctx.stroke();
                }

                curX = 80 + maxStitches * 9.5;
                curY = 200;
                status = 'STITCHING: NEEDLE DOWN (SOLID STITCH)';
                isDown = true;

                if (simFrame >= 44 && simFrame < 58) {
                    ctx.fillStyle = '#F59E0B';
                    ctx.font = 'bold 16px Inter';
                    ctx.fillText('✂️ AUTO-TRIM (કાતર સક્રિય)', 300, 205);
                    status = 'AUTO-TRIM: CUTTING THREAD (કાતર ચાલુ)';
                    curX = 300; curY = 200;
                    isDown = false;
                    zStroke = 'HIGH (TRIM)';
                    currentRpm = '200 RPM (SLOW)';
                    if (simFrame === 45) playSewingSound(true, false);
                } else if (simFrame >= 58 && simFrame < 92) {
                    const jProg = (simFrame - 58) / 34.0;
                    curX = 300 + jProg * 280;
                    curY = 200;
                    ctx.strokeStyle = '#38BDF8';
                    ctx.setLineDash([8, 8]);
                    ctx.lineWidth = 2.5;
                    ctx.beginPath(); ctx.moveTo(300, 200); ctx.lineTo(curX, 200); ctx.stroke();
                    ctx.setLineDash([]);
                    status = 'JUMP: NEEDLE HIGH (DOTTED JUMP VECTOR)';
                    isDown = false;
                    zStroke = 'HIGH (+12mm JUMP)';
                    currentRpm = '1050 RPM (RAPID FRAME)';
                    if (simFrame % 4 === 0) playSewingSound(false, true);
                } else if (simFrame >= 92) {
                    ctx.strokeStyle = '#38BDF8';
                    ctx.setLineDash([8, 8]);
                    ctx.lineWidth = 2.5;
                    ctx.beginPath(); ctx.moveTo(300, 200); ctx.lineTo(580, 200); ctx.stroke();
                    ctx.setLineDash([]);

                    const obj2Stitches = Math.min(22, Math.floor((simFrame - 92) / 1.5));
                    ctx.strokeStyle = '#10B981';
                    ctx.lineWidth = 3.5;
                    for (let i = 0; i < obj2Stitches; i++) {
                        const sx = 600 + i * 9.5;
                        ctx.beginPath();
                        ctx.moveTo(sx, 130 + (i % 2) * 130);
                        ctx.lineTo(sx, 160 + (i % 2) * 130);
                        ctx.stroke();
                    }
                    curX = 600 + obj2Stitches * 9.5;
                    curY = 200;
                    status = 'OBJECT 2: GREEN SATIN STITCHES ACTIVE';
                    isDown = true;
                    if (simFrame % 2 === 0) playSewingSound(false, false);
                } else {
                    if (simFrame % 2 === 0) playSewingSound(false, false);
                }

            } else if (scenario === 'looping') {
                // Scenario 2: Looping / Chenille / Moss Stitch
                ctx.fillStyle = '#1E3A8A';
                ctx.fillRect(60, 230, w - 120, 25);
                ctx.fillStyle = '#FFFFFF';
                ctx.font = '12px Inter';
                ctx.fillText('Navy Velvet Fabric Surface (કાપડની સપાટી)', 70, 247);

                const totalLoops = Math.min(15, Math.floor(simFrame / 5));
                for (let i = 0; i < totalLoops; i++) {
                    const lx = 90 + i * 50;
                    ctx.fillStyle = '#FEF08A';
                    ctx.strokeStyle = '#CA8A04';
                    ctx.lineWidth = 3;
                    ctx.beginPath();
                    ctx.ellipse(lx, 190, 14, 38, 0, 0, Math.PI * 2);
                    ctx.fill(); ctx.stroke();
                    ctx.fillStyle = '#EF4444';
                    ctx.beginPath(); ctx.arc(lx, 230, 3, 0, Math.PI * 2); ctx.fill();
                }

                curX = 90 + totalLoops * 50;
                curY = 210;
                // Rotating Looper hook beneath cloth
                const hookAng = simFrame * 0.5;
                const hx = curX + Math.cos(hookAng) * 20;
                const hy = 265 + Math.sin(hookAng) * 10;
                ctx.strokeStyle = '#A855F7';
                ctx.lineWidth = 4;
                ctx.beginPath(); ctx.moveTo(curX, 245); ctx.lineTo(hx, hy); ctx.stroke();

                status = 'CHENILLE LOOPING: HOLLOW NEEDLE & ROTATING HOOK (LOOP: 3.0mm)';
                currentRpm = '520 RPM (CONTROLLED)';
                zStroke = 'STROKE: 45mm';
                if (simFrame % 3 === 0) playSewingSound(false, false);

            } else if (scenario === 'sequin_fish') {
                // Scenario 3: Sequin Fish-Scale Overlap & Fix Type 26
                const totalSeq = Math.min(12, Math.floor(simFrame / 7));
                for (let i = 0; i < totalSeq; i++) {
                    const sx = 100 + i * 58;
                    const sy = 210 + Math.sin(i * 0.5) * 25;
                    ctx.fillStyle = '#FDE047';
                    ctx.strokeStyle = '#B45309';
                    ctx.lineWidth = 2;
                    ctx.beginPath(); ctx.arc(sx, sy, 26, 0, Math.PI * 2); ctx.fill(); ctx.stroke();
                    // Glint
                    ctx.strokeStyle = '#FFFFFF';
                    ctx.lineWidth = 2;
                    ctx.beginPath(); ctx.arc(sx, sy, 20, 3.5, 5.0); ctx.stroke();
                    // Hole
                    ctx.fillStyle = '#0F172A';
                    ctx.beginPath(); ctx.arc(sx, sy, 5, 0, Math.PI * 2); ctx.fill();
                    // Fix 26 Triangle Lock
                    ctx.strokeStyle = '#EF4444';
                    ctx.lineWidth = 2.5;
                    for (let a of [Math.PI/2, Math.PI*7/6, Math.PI*11/6]) {
                        ctx.beginPath(); ctx.moveTo(sx, sy); ctx.lineTo(sx + Math.cos(a)*20, sy + Math.sin(a)*20); ctx.stroke();
                    }
                }
                curX = 100 + totalSeq * 58;
                curY = 210;
                status = 'SEQUIN CHUTE: 3mm DROP + 40% OVERLAP + FIX TYPE 26 TRIANGLE LOCK';
                currentRpm = '750 RPM';
                if (simFrame % 4 === 0) playSewingSound(false, false);

            } else if (scenario === 'sequin_stack') {
                // Scenario 4: Double Sequin Stacking
                const totalStacks = Math.min(8, Math.floor(simFrame / 10));
                for (let i = 0; i < totalStacks; i++) {
                    const sx = 120 + i * 85;
                    const sy = 210;
                    // 5mm Gold base
                    ctx.fillStyle = '#FDE047';
                    ctx.strokeStyle = '#B45309';
                    ctx.lineWidth = 2;
                    ctx.beginPath(); ctx.arc(sx, sy, 34, 0, Math.PI * 2); ctx.fill(); ctx.stroke();
                    // 3mm Silver Top
                    ctx.fillStyle = '#E2E8F0';
                    ctx.strokeStyle = '#38BDF8';
                    ctx.lineWidth = 2;
                    ctx.beginPath(); ctx.arc(sx, sy, 20, 0, Math.PI * 2); ctx.fill(); ctx.stroke();
                    // Hole & Star lock
                    ctx.fillStyle = '#0F172A';
                    ctx.beginPath(); ctx.arc(sx, sy, 4.5, 0, Math.PI * 2); ctx.fill();
                    ctx.strokeStyle = '#EF4444';
                    ctx.lineWidth = 2;
                    for (let a of [0, Math.PI/2, Math.PI, Math.PI*3/2]) {
                        ctx.beginPath(); ctx.moveTo(sx, sy); ctx.lineTo(sx + Math.cos(a)*15, sy + Math.sin(a)*15); ctx.stroke();
                    }
                }
                curX = 120 + totalStacks * 85;
                curY = 210;
                status = 'DUAL SEQUIN: CHUTE A (5mm) + CHUTE B (3mm) CONCENTRIC STAR LOCK';
                currentRpm = '680 RPM';
                if (simFrame % 5 === 0) playSewingSound(false, false);

            } else if (scenario === 'beads_taka') {
                // Scenario 5: Beads & Cutdana Taka Distance
                const pearls = Math.min(10, Math.floor(simFrame / 6));
                for (let i = 0; i < pearls; i++) {
                    const px = 90 + i * 65;
                    ctx.fillStyle = '#F8FAFC';
                    ctx.strokeStyle = '#94A3B8';
                    ctx.lineWidth = 2;
                    ctx.beginPath(); ctx.arc(px, 140, 16, 0, Math.PI * 2); ctx.fill(); ctx.stroke();
                    ctx.fillStyle = '#FFFFFF';
                    ctx.beginPath(); ctx.arc(px - 5, 135, 5, 0, Math.PI * 2); ctx.fill();
                    ctx.strokeStyle = '#EF4444';
                    ctx.lineWidth = 2.5;
                    ctx.beginPath(); ctx.moveTo(px - 22, 140); ctx.lineTo(px + 22, 140); ctx.stroke();
                }

                const pipes = Math.min(6, Math.floor(simFrame / 9));
                for (let i = 0; i < pipes; i++) {
                    const bx = 110 + i * 110;
                    ctx.fillStyle = '#FEF08A';
                    ctx.strokeStyle = '#CA8A04';
                    ctx.lineWidth = 2;
                    ctx.fillRect(bx - 36, 260, 72, 22);
                    ctx.strokeRect(bx - 36, 260, 72, 22);
                    ctx.strokeStyle = '#EF4444';
                    ctx.lineWidth = 2.5;
                    ctx.beginPath(); ctx.moveTo(bx - 45, 271); ctx.lineTo(bx + 45, 271); ctx.stroke();
                }
                curX = 110 + pipes * 110;
                curY = 271;
                status = 'BEADS TRACK: ROUND PEARL TAKA 2.30mm | CUTDANA GLASS PIPE 4.50mm';
                currentRpm = '650 RPM';
                if (simFrame % 4 === 0) playSewingSound(false, false);

            } else if (scenario === 'beads_curve') {
                // Scenario 6: Curved Path 9° Rotation
                const pts = min(14, Math.floor(simFrame / 5));
                for (let i = 0; i < pts; i++) {
                    const tx = 90 + i * 50;
                    const ty = 210 + Math.sin(tx / 65) * 65;
                    const slope = Math.cos(tx / 65);
                    const ang = Math.round(Math.atan(slope) * 180 / Math.PI / 9) * 9 * Math.PI / 180;
                    if (i % 2 === 0) {
                        ctx.fillStyle = '#F8FAFC';
                        ctx.strokeStyle = '#38BDF8';
                        ctx.lineWidth = 2;
                        ctx.beginPath(); ctx.arc(tx, ty, 13, 0, Math.PI * 2); ctx.fill(); ctx.stroke();
                    } else {
                        const dx = Math.cos(ang) * 18;
                        const dy = Math.sin(ang) * 18;
                        ctx.strokeStyle = '#F59E0B';
                        ctx.lineWidth = 8;
                        ctx.beginPath(); ctx.moveTo(tx - dx, ty - dy); ctx.lineTo(tx + dx, ty + dy); ctx.stroke();
                    }
                }
                curX = 90 + pts * 50;
                curY = 210 + Math.sin(curX / 65) * 65;
                status = 'S-CURVE NECKLINE: BEADS ROTATING TANGENT IN 9° STEPS (Alt+CapsLock)';
                currentRpm = '600 RPM';
                if (simFrame % 3 === 0) playSewingSound(false, false);

            } else if (scenario === 'flower_cluster') {
                // Scenario 7: Bridal Flower Cluster (Pearl Center + Sequin Petals)
                const fcx = w / 2, fcy = 210;
                // Stem
                ctx.strokeStyle = '#10B981';
                ctx.lineWidth = 4;
                ctx.beginPath(); ctx.moveTo(fcx, fcy + 40); ctx.quadraticCurveTo(fcx - 30, fcy + 100, fcx - 20, fcy + 140); ctx.stroke();

                // Petals
                const petals = Math.min(6, Math.floor(simFrame / 8));
                for (let i = 0; i < petals; i++) {
                    const a = i * (Math.PI * 2 / 6);
                    const px = fcx + Math.cos(a) * 45;
                    const py = fcy + Math.sin(a) * 45;
                    ctx.fillStyle = '#FEF08A';
                    ctx.strokeStyle = '#CA8A04';
                    ctx.lineWidth = 2;
                    ctx.beginPath(); ctx.arc(px, py, 22, 0, Math.PI * 2); ctx.fill(); ctx.stroke();
                    ctx.fillStyle = '#EF4444';
                    ctx.beginPath(); ctx.arc(px, py, 4, 0, Math.PI * 2); ctx.fill();
                }
                // Center pearl
                if (simFrame > 20) {
                    ctx.fillStyle = '#F8FAFC';
                    ctx.strokeStyle = '#94A3B8';
                    ctx.lineWidth = 2.5;
                    ctx.beginPath(); ctx.arc(fcx, fcy, 18, 0, Math.PI * 2); ctx.fill(); ctx.stroke();
                    ctx.fillStyle = '#FFFFFF';
                    ctx.beginPath(); ctx.arc(fcx - 5, fcy - 5, 6, 0, Math.PI * 2); ctx.fill();
                }
                curX = fcx + Math.cos(petals * Math.PI / 3) * 45;
                curY = fcy + Math.sin(petals * Math.PI / 3) * 45;
                status = 'BRIDAL CLUSTER: CENTER PEARL BEAD + 6 METALLIC SEQUIN PETALS';
                currentRpm = '720 RPM';
                if (simFrame % 3 === 0) playSewingSound(false, false);

            } else if (scenario === 'paghdi') {
                // Scenario 8: Paghdi F4 Column Symmetry
                const cx = w / 2;
                const pProg = Math.min(1.0, simFrame / 80);
                const maxSteps = Math.floor(pProg * 40);
                ctx.strokeStyle = '#F59E0B';
                ctx.lineWidth = 3;
                for (let i = 0; i < maxSteps; i++) {
                    const py = 90 + i * 5.5;
                    const halfW = 35 + Math.sin(i * 0.15) * 55;
                    ctx.beginPath(); ctx.moveTo(cx - halfW, py); ctx.lineTo(cx + halfW, py); ctx.stroke();
                }
                ctx.strokeStyle = '#38BDF8';
                ctx.lineWidth = 2;
                ctx.beginPath();
                for (let i = 0; i < 40; i++) {
                    const py = 90 + i * 5.5;
                    const halfW = 35 + Math.sin(i * 0.15) * 55;
                    if (i === 0) ctx.moveTo(cx - halfW, py); else ctx.lineTo(cx - halfW, py);
                }
                ctx.stroke();
                ctx.beginPath();
                for (let i = 0; i < 40; i++) {
                    const py = 90 + i * 5.5;
                    const halfW = 35 + Math.sin(i * 0.15) * 55;
                    if (i === 0) ctx.moveTo(cx + halfW, py); else ctx.lineTo(cx + halfW, py);
                }
                ctx.stroke();
                curX = cx;
                curY = 90 + maxSteps * 5.5;
                status = 'F4 COLUMN SYMMETRY: SATIN FILL DENSITY (WIDTH 1100 = 0.8 - 1.1mm)';
                currentRpm = '850 RPM';
                if (simFrame % 2 === 0) playSewingSound(false, false);

            } else if (scenario === 'origin') {
                // Scenario 9: DR 250 Origin Lock
                ctx.strokeStyle = '#38BDF8';
                ctx.lineWidth = 2.5;
                ctx.beginPath(); ctx.arc(100, 210, 14, 0, Math.PI * 2); ctx.stroke();
                ctx.fillStyle = '#38BDF8';
                ctx.font = '12px Inter';
                ctx.fillText('ORIGIN DR 250 (0,0)', 50, 240);

                ctx.strokeStyle = '#F59E0B';
                ctx.lineWidth = 2;
                ctx.strokeRect(420, 120, 180, 180);
                ctx.fillStyle = '#FFFFFF';
                ctx.fillText('Embroidery Motif (Flower)', 450, 105);

                if (simFrame < 20) {
                    const p = simFrame / 20;
                    curX = 100 + p * 320;
                    curY = 210;
                    status = 'FRAME TRAVEL: FROM ORIGIN DR 250 TO MOTIF START POINT';
                    isDown = false;
                } else if (simFrame < 28) {
                    curX = 420; curY = 210;
                    status = 'TIE-IN: 3 MICRO LOCK STITCHES (દોરો બાંધવો)';
                    isDown = true;
                } else if (simFrame < 80) {
                    curX = 420 + Math.random() * 180;
                    curY = 120 + Math.random() * 180;
                    status = 'STITCHING MOTIF EMBROIDERY';
                    isDown = true;
                } else if (simFrame < 92) {
                    curX = 600; curY = 210;
                    status = 'TIE-OFF: 4 LOCK STITCHES + AUTO-TRIM';
                    isDown = true;
                } else {
                    const p = (simFrame - 92) / 38;
                    curX = 600 - p * 500;
                    curY = 210;
                    status = 'RETURNING TO DR 250 ORIGIN (MACHINE PARKED AT 0,0)';
                    isDown = false;
                }
                if (simFrame % 3 === 0) playSewingSound(false, !isDown);
            }

            // Reset shadow before drawing chrome needle assembly
            ctx.shadowColor = 'transparent';
            drawNeedleHead(ctx, curX, curY, isDown, 45, threadColor);

            if (statusEl) statusEl.innerText = status;
            if (coordsEl) coordsEl.innerText = `X=${Math.round(curX)} mm, Y=${Math.round(curY)} mm`;
            if (countEl) countEl.innerText = `${simFrame * 9} TAKA (${Math.round((simFrame/140)*100)}%)`;
            if (rpmEl) rpmEl.innerText = currentRpm;
            if (strokeEl) strokeEl.innerText = zStroke;
        }

        // Initialize simulator on page load
        window.addEventListener('load', function() {
            drawSimFrame();
        });

        // --- QUIZ LOGIC ---
        let userAnswers = {};
        function checkAnswer(el, chosenIdx) {
            const card = el.closest('.quiz-card');
            const correctIdx = parseInt(card.getAttribute('data-correct'));
            const options = card.querySelectorAll('.quiz-option');
            const feedback = card.querySelector('.quiz-feedback');

            options.forEach(opt => {
                opt.classList.remove('correct', 'wrong');
            });

            if (chosenIdx === correctIdx) {
                el.classList.add('correct');
                feedback.style.display = 'block';
                feedback.style.background = '#ECFDF5';
                feedback.style.color = '#065F46';
                feedback.innerHTML = '<b>✅ સાચો જવાબ!</b> શાબાશ, તમારો કોન્સેપ્ટ એકદમ સાચો છે.';
                userAnswers[card.innerText.slice(0, 10)] = true;
            } else {
                el.classList.add('wrong');
                options[correctIdx].classList.add('correct');
                feedback.style.display = 'block';
                feedback.style.background = '#FEF2F2';
                feedback.style.color = '#991B1B';
                feedback.innerHTML = '<b>❌ ખોટો જવાબ!</b> સાચો વિકલ્પ લીલા રંગથી હાઇલાઇટ કર્યો છે. નિયમ ફરી ધ્યાનથી વાંચો.';
                userAnswers[card.innerText.slice(0, 10)] = false;
            }

            // Update total score
            const cards = document.querySelectorAll('.quiz-card');
            let score = 0;
            let answered = 0;
            cards.forEach(c => {
                const checked = c.querySelector('.quiz-option.correct');
                if (checked) {
                    answered++;
                    const wasUser = checked.parentElement.querySelector('.quiz-option.wrong');
                    if (!wasUser) score++;
                }
            });

            if (answered >= 5) {
                const scoreBox = document.getElementById('quizScoreBox');
                const scoreEl = document.getElementById('quizScore');
                const msgEl = document.getElementById('quizScoreMsg');
                if (scoreBox && scoreEl && msgEl) {
                    scoreBox.style.display = 'block';
                    scoreEl.innerText = score;
                    if (score >= 8) {
                        msgEl.innerText = '🎉 અભિનંદન! તમે EmCAD પંચિંગ માસ્ટર બનવા માટે સંપૂર્ણ લાયકાત ધરાવો છો! (Certified Punching Master)';
                    } else {
                        msgEl.innerText = '👍 સારો પ્રયાસ! બાકી રહેલા નિયમો અને શોર્ટકટ્સ ફરી એકવાર રીવાઇઝ કરો.';
                    }
                }
            }
        }

    </script>
</body>
</html>
"""

def assemble_sections():
    # Use raw string formatting to avoid escaping issues
    sec1 = """
    <div class="section-card" id="sec-tools">
        <div class="section-header">
            <div class="section-title">
                <span>🛠️</span> Section 1: Tools & Symbols Reference (Tools 01 to 52)
            </div>
            <span class="section-tag">ટૂલ્સ ૧ થી ૫૨ સંપુર્ણ પરિચય</span>
        </div>
        <p style="margin-bottom: 16px;">
            EmCAD સોફ્ટવેરમાં ડાબી બાજુ, જમણી બાજુ અને ટોપ ટૂલબારમાં કુલ <b>૫૨ મુખ્ય ટૂલ્સ</b> આવેલા છે. 
            નીચે તમારી રેફરન્સ બુકના તમામ ઓરિજિનલ પેજના હાઇ-રિઝોલ્યુશન ચિત્રો અને દરેક ટૂલનું વિસ્તૃત ટેબલ આપેલું છે:
        </p>

        <div class="image-gallery">
            """ + img_card("01_Tools_Symbols_Part1_Tools_01_to_11.jpg", "ટૂલ્સ ૦૧ થી ૧૧", "Select, Polygon Select, Shape Edit (H), Edit Stitch (E), Sequin, Color, Stop, Trim, Tie") + """
            """ + img_card("02_Tools_Symbols_Part2_Tools_11_to_21.jpg", "ટૂલ્સ ૧૧ થી ૨૧", "Jump Stitch, Normal Stitch, Connectors, Delete, Move, Zoom (Z), Pan, Grid, View Modes") + """
            """ + img_card("03_Tools_Symbols_Part3_Tools_22_to_32.jpg", "ટૂલ્સ ૨૨ થી ૩૨", "Measuring Tape, Vector Shapes (Rectangle, Circle, Star), Outline, Offset, Curve Smooth") + """
            """ + img_card("04_Tools_Symbols_Part4_Tools_33_to_43.jpg", "ટૂલ્સ ૩૩ થી ૪૩", "Break, Weld, Divide, Trim Vector, Angle Lines, Density Adjustment, Underlay Settings") + """
            """ + img_card("05_Tools_Symbols_Part5_Tools_44_to_52.jpg", "ટૂલ્સ ૪૪ થી ૫૨", "Manual Run, Jump 1000/100/10, Slow Replay, Origin Set, Print Preview, Export Data") + """
        </div>

        <h3 style="margin: 20px 0 10px 0; color: var(--primary);">📋 Complete 52 Tools Master Table</h3>
        <div style="overflow-x: auto;">
        <table class="data-table">
            <thead>
                <tr>
                    <th style="width: 50px;">No.</th>
                    <th style="width: 170px;">ટૂલ નામ (Tool Name)</th>
                    <th style="width: 110px;">શોર્ટકટ કી</th>
                    <th style="width: 130px;">સિમ્બોલ ઓળખ</th>
                    <th>પ્રેક્ટિકલ ઉપયોગ અને પંચિંગ સમજૂતી (Detailed Function)</th>
                </tr>
            </thead>
            <tbody>
                <tr><td><span class="badge-num">01</span></td><td><b>Select</b></td><td><span class="badge-code">Space / Arrow</span></td><td>Pointer Arrow</td><td><b>સિલેક્ટ કરવા માટે:</b> સ્ક્રીન પર કોઈપણ ઓબ્જેક્ટ, લાઇન કે શેપને પસંદ કરવા.</td></tr>
                <tr><td><span class="badge-num">02</span></td><td><b>Select Current Stitch</b></td><td><span class="badge-code">Click on Wand</span></td><td>Stitch Wand</td><td><b>ચાલુ ટાંકાનો ઓબ્જેક્ટ સિલેક્ટ કરવા:</b> કર્સર જે સ્ટીચ પર હોય તે આખો ઓબ્જેક્ટ આપોઆપ સિલેક્ટ થાય.</td></tr>
                <tr><td><span class="badge-num">03</span></td><td><b>Polygon Select</b></td><td><span class="badge-code">Ctrl + L</span></td><td>Lasso / Poly</td><td><b>પોલીગોન સિલેક્શન:</b> અનિયમિત આકારમાં લાસો દોરીને જોઈએ તેટલો જ ભાગ સિલેક્ટ કરવા.</td></tr>
                <tr><td><span class="badge-num">04</span></td><td><b>Section Select</b></td><td><span class="badge-code">Section Tool</span></td><td>Dividing Line</td><td><b>સેક્શન સિલેક્ટ:</b> એક લાઇન દોરીને વચ્ચેથી પસાર થતા ઓબ્જેક્ટ્સને એકસાથે સિલેક્ટ કરવા.</td></tr>
                <tr><td><span class="badge-num">05</span></td><td><b>Shape Edit</b></td><td><span class="badge-code">H</span></td><td>Node Reshaper</td><td><b>શેપ એડિટિંગ:</b> ઓબ્જેક્ટના પોઇન્ટ્સ (Nodes), વળાંકો અને એંગલ બદલવા.</td></tr>
                <tr><td><span class="badge-num">06</span></td><td><b>Edit Stitch</b></td><td><span class="badge-code">E</span></td><td>Single Needle</td><td><b>સ્ટીચ એડિટ:</b> સિંગલ સ્ટીચ લેવલ પર ટાંકો ડિલીટ કરવા, ખસેડવા કે મોડીફાય કરવા.</td></tr>
                <tr><td><span class="badge-num">07</span></td><td><b>Edit Sequin</b></td><td><span class="badge-code">Sequin Tool</span></td><td>Disc & Needle</td><td><b>સિક્વિન એડિટ:</b> સિક્વિન ડ્રોપ, અંતર કે દિશામાં ફેરફાર કરવા માટે.</td></tr>
                <tr><td><span class="badge-num">08</span></td><td><b>Color Change</b></td><td><span class="badge-code">Flower Icon</span></td><td>6-Petal Flower</td><td><b>કલર / સોય બદલવા:</b> મલ્ટી-કલર ડિઝાઇનમાં સોય (Needle / Stop) બદલવાનો કમાન્ડ આપવા.</td></tr>
                <tr><td><span class="badge-num">09</span></td><td><b>Stop</b></td><td><span class="badge-code">Stop Command</span></td><td>Stop Octagon</td><td><b>મશીન સ્ટોપ:</b> એપ્લિક મૂકવા કે દોરો બદલવા મશીનને ઊભું રાખવા સ્ટોપ કમાન્ડ આપવો.</td></tr>
                <tr><td><span class="badge-num">10</span></td><td><b>Trim</b></td><td><span class="badge-code">Scissors</span></td><td>Scissor Icon</td><td><b>દોરો કાપવા (Trim):</b> એક ભાગ પત્યા પછી બીજા ભાગ પર જતાં દોરો કાપવાનો કમાન્ડ.</td></tr>
                <tr><td><span class="badge-num">11</span></td><td><b>Tie</b></td><td><span class="badge-code">Knot / Arrow</span></td><td>Tie-on/Tie-off</td><td><b>ટાઇ સ્ટીચ (ગાંઠ):</b> શરૂઆતમાં અને છેલ્લે દોરો ઉકલી ન જાય તે માટે લોક ટાંકા આપવા.</td></tr>
                <tr><td><span class="badge-num">12</span></td><td><b>Jump Stitch</b></td><td><span class="badge-code">J / Shift + J</span></td><td>Dotted Line</td><td><b>જમ્પ સ્ટીચ:</b> સોય ચાલ્યા વગર ફ્રેમ ખસેડવા (ટાંકો ન પડે તેવો જમ્પ).</td></tr>
                <tr><td><span class="badge-num">13</span></td><td><b>Normal Stitch</b></td><td><span class="badge-code">N</span></td><td>Solid Line</td><td><b>સામાન્ય ટાંકો:</b> જમ્પમાંથી સામાન્ય સ્ટીચ મોડમાં પાછા ફરવા.</td></tr>
                <tr><td><span class="badge-num">14</span></td><td><b>Connectors</b></td><td><span class="badge-code">Ctrl + K</span></td><td>Link Chain</td><td><b>કનેક્ટર્સ:</b> બે ઓબ્જેક્ટ વચ્ચે કનેક્શન (જમ્પ કે રન) સેટ કરવા.</td></tr>
                <tr><td><span class="badge-num">15</span></td><td><b>Delete</b></td><td><span class="badge-code">Delete / Backspace</span></td><td>Trash / Cross</td><td><b>ડિલીટ:</b> પસંદ કરેલા ઓબ્જેક્ટ કે ટાંકાને દૂર કરવા.</td></tr>
                <tr><td><span class="badge-num">16</span></td><td><b>Move / Nudge</b></td><td><span class="badge-code">Arrow Keys</span></td><td>4-Way Arrow</td><td><b>ખસેડવા:</b> ઓબ્જેક્ટને ચોક્કસ દિશામાં 0.1 mm કે 1 mm ખસેડવા.</td></tr>
                <tr><td><span class="badge-num">17</span></td><td><b>Rotate</b></td><td><span class="badge-code">Ctrl + R</span></td><td>Curved Arrow</td><td><b>ગોળ ફેરવવા:</b> ઓબ્જેક્ટને ચોક્કસ ડિગ્રીમાં ગોળ ફેરવવા.</td></tr>
                <tr><td><span class="badge-num">18</span></td><td><b>Scale / Resize</b></td><td><span class="badge-code">Ctrl + S</span></td><td>Resize Box</td><td><b>માપ બદલવું:</b> ડિઝાઇન કે ઓબ્જેક્ટનું માપ ટકાવારીમાં કે mm માં નાનું-મોટું કરવા.</td></tr>
                <tr><td><span class="badge-num">19</span></td><td><b>Mirror Horizontal</b></td><td><span class="badge-code">R -> X</span></td><td>Flip H</td><td><b>આડો અરીસો:</b> ડાબેથી જમણે મિરર (પ્રતિબિંબ) કરવા.</td></tr>
                <tr><td><span class="badge-num">20</span></td><td><b>Mirror Vertical</b></td><td><span class="badge-code">R -> Y</span></td><td>Flip V</td><td><b>ઊભો અરીસો:</b> ઉપરથી નીચે મિરર કરવા.</td></tr>
                <tr><td><span class="badge-num">21</span></td><td><b>Zoom In / Out</b></td><td><span class="badge-code">Z / F2 / Scroll</span></td><td>Magnifier</td><td><b>ઝૂમ:</b> સ્ક્રીનને મોટી કે નાની કરીને ઝીણવટપૂર્વક જોવા.</td></tr>
                <tr><td><span class="badge-num">22</span></td><td><b>Pan Screen</b></td><td><span class="badge-code">Middle Mouse Drag</span></td><td>Hand Tool</td><td><b>સ્ક્રીન પેન:</b> સ્ક્રીનને કોઈપણ દિશામાં ખસેડીને જોવા.</td></tr>
                <tr><td><span class="badge-num">23</span></td><td><b>Fit to Screen</b></td><td><span class="badge-code">0 (Zero) / F4</span></td><td>Fit Box</td><td><b>સ્ક્રીન ફિટ:</b> આખી ડિઝાઇન એકસાથે સ્ક્રીન પર ફિટ કરીને જોવા.</td></tr>
                <tr><td><span class="badge-num">24</span></td><td><b>Show / Hide Grid</b></td><td><span class="badge-code">Shift + G</span></td><td>Grid Lines</td><td><b>ગ્રીડ લાઇન્સ:</b> ચોરસ ગ્રીડ લાઇન્સ ઓન કે ઓફ કરવા.</td></tr>
                <tr><td><span class="badge-num">25</span></td><td><b>Measure Tape</b></td><td><span class="badge-code">M</span></td><td>Ruler Icon</td><td><b>માપપટ્ટી:</b> સ્ક્રીન પર બે પોઇન્ટ વચ્ચેનું ચોક્કસ અંતર mm માં માપવા.</td></tr>
                <tr><td><span class="badge-num">26</span></td><td><b>Guide Lines</b></td><td><span class="badge-code">Drag from Ruler</span></td><td>Dashed Ruler</td><td><b>ગાઈડલાઈન:</b> આડી કે ઊભી ગાઈડલાઈન મૂકીને અલાઇનમેન્ટ કરવા.</td></tr>
                <tr><td><span class="badge-num">27</span></td><td><b>Snap to Grid</b></td><td><span class="badge-code">Alt + G</span></td><td>Magnet & Grid</td><td><b>ગ્રીડ સ્નેપ:</b> પોઇન્ટ્સ આપોઆપ ગ્રીડ લાઇન પર ચોંટી જાય તે માટે.</td></tr>
                <tr><td><span class="badge-num">28</span></td><td><b>Rectangle Tool</b></td><td><span class="badge-code">Rect Icon</span></td><td>Square Box</td><td><b>લંબચોરસ:</b> ચોરસ કે લંબચોરસ વેક્ટર બોક્સ દોરવા.</td></tr>
                <tr><td><span class="badge-num">29</span></td><td><b>Ellipse / Circle</b></td><td><span class="badge-code">Circle Icon</span></td><td>Round Circle</td><td><b>વર્તુળ:</b> ગોળ કે લંબગોળ શેપ દોરવા.</td></tr>
                <tr><td><span class="badge-num">30</span></td><td><b>Polyline Tool</b></td><td><span class="badge-code">Line Icon</span></td><td>Segmented Line</td><td><b>પોલીલાઇન:</b> ખુલ્લી કે બંધ સીધી રેખાઓ દોરવા.</td></tr>
                <tr><td><span class="badge-num">31</span></td><td><b>Bezier Curve</b></td><td><span class="badge-code">Curve Icon</span></td><td>Smooth S-Curve</td><td><b>બેઝિયર કર્વ:</b> સ્મૂથ વળાંકવાળી રેખાઓ દોરવા.</td></tr>
                <tr><td><span class="badge-num">32</span></td><td><b>Freehand Draw</b></td><td><span class="badge-code">Pencil Icon</span></td><td>Freehand Pen</td><td><b>ફ્રીહેન્ડ સ્કેચ:</b> હાથેથી મુક્ત સ્કેચિંગ કરવા.</td></tr>
                <tr><td><span class="badge-num">33</span></td><td><b>Break Object</b></td><td><span class="badge-code">B</span></td><td>Split Line</td><td><b>બ્રેક લાઇન:</b> કોઈપણ લાઇન કે ઓબ્જેક્ટને એક પોઇન્ટ પરથી તોડીને બે ભાગ કરવા.</td></tr>
                <tr><td><span class="badge-num">34</span></td><td><b>Weld / Combine</b></td><td><span class="badge-code">J</span></td><td>Intersect Shapes</td><td><b>વેલ્ડ (જોડાણ):</b> બે અલગ અલગ ઓબ્જેક્ટ્સને જોડીને એક બનાવી દેવા.</td></tr>
                <tr><td><span class="badge-num">35</span></td><td><b>Divide Object</b></td><td><span class="badge-code">Divide Tool</span></td><td>Knife Cutting</td><td><b>ડિવાઇડ:</b> એક શેપને બીજા શેપ વડે વચ્ચેથી કાપીને અલગ કરવા.</td></tr>
                <tr><td><span class="badge-num">36</span></td><td><b>Trim Vector</b></td><td><span class="badge-code">Ctrl + T</span></td><td>Scissor on Line</td><td><b>વેક્ટર ટ્રીમ:</b> વધારાની બહાર નીકળતી વેક્ટર લાઇન કાપી નાખવા.</td></tr>
                <tr><td><span class="badge-num">37</span></td><td><b>Offset Object</b></td><td><span class="badge-code">Offset Tool</span></td><td>Parallel Rings</td><td><b>ઓફસેટ:</b> ઓબ્જેક્ટની ચોતરફ ચોક્કસ mm ના અંતરે નવી લાઇન બનાવવી.</td></tr>
                <tr><td><span class="badge-num">38</span></td><td><b>Smooth Curve</b></td><td><span class="badge-code">Smooth Tool</span></td><td>Curved Wave</td><td><b>સ્મૂથ વળાંક:</b> વળાંકના પોઇન્ટ્સ ઘટાડી લાઇનને એકદમ લીસી બનાવવી.</td></tr>
                <tr><td><span class="badge-num">39</span></td><td><b>Align Objects</b></td><td><span class="badge-code">Ctrl + Shift + A</span></td><td>Align Bars</td><td><b>અલાઇનમેન્ટ:</b> ઓબ્જેક્ટ્સને ડાબે, જમણે, સેન્ટરમાં એક લાઇન કરવા.</td></tr>
                <tr><td><span class="badge-num">40</span></td><td><b>Distribute</b></td><td><span class="badge-code">Distribute Tool</span></td><td>Equal Spacing</td><td><b>સરખું અંતર:</b> બધા ઓબ્જેક્ટ્સ વચ્ચે એકસરખું અંતર રાખવા.</td></tr>
                <tr><td><span class="badge-num">41</span></td><td><b>Group Objects</b></td><td><span class="badge-code">Ctrl + G</span></td><td>Group Box</td><td><b>ગ્રૂપ:</b> ઘણા બધા ઓબ્જેક્ટ્સને એક ગ્રૂપ બનાવી સાથે ફેરવવા.</td></tr>
                <tr><td><span class="badge-num">42</span></td><td><b>Ungroup</b></td><td><span class="badge-code">Ctrl + U</span></td><td>Ungroup Box</td><td><b>અનગ્રૂપ:</b> ગ્રૂપ છૂટું પાડવા.</td></tr>
                <tr><td><span class="badge-num">43</span></td><td><b>Stitch Angle</b></td><td><span class="badge-code">Angle Tool</span></td><td>Needle Angle</td><td><b>સ્ટીચ એંગલ:</b> સાટિન કે તતામીના ટાંકાનો ખૂણો (Angle) બદલવા.</td></tr>
                <tr><td><span class="badge-num">44</span></td><td><b>Density Edit</b></td><td><span class="badge-code">Density Tool</span></td><td>Thick/Thin Lines</td><td><b>ડેન્સિટી (ઘનતા):</b> ટાંકા કેટલા નજીક કે દૂર પડશે તે અંતર (0.4-0.8 mm) બદલવા.</td></tr>
                <tr><td><span class="badge-num">45</span></td><td><b>Underlay Setup</b></td><td><span class="badge-code">Underlay Tool</span></td><td>Mesh Foundation</td><td><b>અંડરલે:</b> મુખ્ય ટાંકા નીચે બેઝ (તળિયા) ના ટાંકા આપવા.</td></tr>
                <tr><td><span class="badge-num">46</span></td><td><b>Pull Compensation</b></td><td><span class="badge-code">Pull Comp Tool</span></td><td>Arrows Outward</td><td><b>પુલ કોમ્પ:</b> કાપડ સંકોચાવા સામે ટાંકા થોડા પહોળા કરવા (0.2-0.4 mm).</td></tr>
                <tr><td><span class="badge-num">47</span></td><td><b>Manual Stitch</b></td><td><span class="badge-code">Manual Run</span></td><td>Single Needle</td><td><b>મેન્યુઅલ ટાંકો:</b> હાથેથી એક-એક ટાંકો મૂકવા.</td></tr>
                <tr><td><span class="badge-num">48</span></td><td><b>Jump 1000 Stitches</b></td><td><span class="badge-code">Page Up / Down</span></td><td>Double Fast Arrow</td><td><b>૧૦૦૦ ટાંકા જમ્પ:</b> ડિઝાઇનમાં એકસાથે ૧૦૦૦ ટાંકા આગળ કે પાછળ જવા.</td></tr>
                <tr><td><span class="badge-num">49</span></td><td><b>Jump 100 Stitches</b></td><td><span class="badge-code">Ctrl + Up / Down</span></td><td>Fast Arrow</td><td><b>૧૦૦ ટાંકા જમ્પ:</b> એકસાથે ૧૦૦ ટાંકા આગળ-પાછળ જવા.</td></tr>
                <tr><td><span class="badge-num">50</span></td><td><b>Jump 10 Stitches</b></td><td><span class="badge-code">Up / Down Arrow</span></td><td>Single Step Arrow</td><td><b>૧૦ ટાંકા જમ્પ:</b> એક-એક કે ૧૦-૧૦ ટાંકા આગળ-પાછળ ચકાસવા.</td></tr>
                <tr><td><span class="badge-num">51</span></td><td><b>Slow Replay</b></td><td><span class="badge-code">Shift + R</span></td><td>Play Movie Icon</td><td><b>સ્લો રિપ્લે:</b> મશીન પર ડિઝાઇન કેવી રીતે ચાલશે તેનું સ્લો સિમ્યુલેશન જોવા.</td></tr>
                <tr><td><span class="badge-num">52</span></td><td><b>Set Machine Origin</b></td><td><span class="badge-code">Ctrl + Home</span></td><td>Crosshair Flag</td><td><b>ઓરિજિન સેટિંગ:</b> મશીનનું ઝીરો પોઇન્ટ (X=0, Y=0 / Start Origin) નક્કી કરવા.</td></tr>
            </tbody>
        </table>
        </div>
    </div>
    """

    sec2 = """
    <div class="section-card" id="sec-units">
        <div class="section-header">
            <div class="section-title">
                <span>📏</span> Section 2: Units & Basic Measurements (Step 2)
            </div>
            <span class="section-tag">એમ્બ્રોઇડરી માપ અને ગણતરી</span>
        </div>
        <p style="margin-bottom: 16px;">
            એમ્બ્રોઇડરી પંચિંગમાં ચોક્કસ માપ વગર ડિઝાઇન મશીન પર ક્યારેય સેટ થઈ શકતી નથી. 
            EmCAD સોફ્ટવેર અને દહાઓ મશીન કંટ્રોલર <b>મિલીમીટર (mm)</b> માં ગણતરી કરે છે, જ્યારે કાપડ અને સાડીનો પન્નો <b>ઇંચ (Inch)</b> માં માપવામાં આવે છે.
        </p>

        <div class="image-gallery">
            """ + img_card("06_Step2_Units_Measurements_Area.jpg", "Step 2: માપ અને મશીન એરિયા ટેબલ", "ઇંચ, મિલીમીટર, મીટર કન્વર્ઝન અને સ્ટાન્ડર્ડ મશીન રીપીટ સાઇઝ") + """
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 20px; margin: 20px 0;">
            <div>
                <h3 style="color: var(--primary); margin-bottom: 8px;">📐 યુનિટ કન્વર્ઝન ટેબલ</h3>
                <table class="data-table">
                    <thead><tr><th>ઇંચ / મીટર</th><th>મિલીમીટર (mm)</th><th>પ્રેક્ટિકલ સંદર્ભ</th></tr></thead>
                    <tbody>
                        <tr><td><b>1 Inch</b></td><td><b>25.4 mm</b></td><td>ગણતરી માટે ૨૫ mm ગણવું</td></tr>
                        <tr><td><b>12 Inch (1 Foot)</b></td><td><b>300 mm</b></td><td>સ્ટાન્ડર્ડ બોક્સ પેટર્ન</td></tr>
                        <tr><td><b>1 Meter</b></td><td><b>1000 mm</b></td><td>39.37 Inch (~ 40 પન્નો)</td></tr>
                        <tr><td><b>40 Inch Panna</b></td><td><b>1000 mm</b></td><td>સામાન્ય સાડી અને ડ્રેસ</td></tr>
                        <tr><td><b>43-44 Inch Panna</b></td><td><b>1100 mm</b></td><td>સ્ટાન્ડર્ડ સિલ્ક સાડી</td></tr>
                        <tr><td><b>48 Inch Panna</b></td><td><b>1200 mm</b></td><td>હેવી સાડી અને લહેંગા</td></tr>
                    </tbody>
                </table>
            </div>

            <div>
                <h3 style="color: var(--primary); margin-bottom: 8px;">⚙️ મશીન રીપીટ સ્ટાન્ડર્ડ સાઇઝ</h3>
                <table class="data-table">
                    <thead><tr><th>રીપીટ સાઇઝ</th><th>ડિઝાઇન પ્રકાર</th><th>પંચિંગ નિયમ</th></tr></thead>
                    <tbody>
                        <tr><td><b>125 mm</b></td><td>ઝીણી લેસ / બુટ્ટી</td><td>1 મીટરમાં 8 રીપીટ બેસે</td></tr>
                        <tr><td><b>250 mm</b></td><td>મીડીયમ બોર્ડર</td><td>1 મીટરમાં 4 રીપીટ બેસે</td></tr>
                        <tr><td><b>300 mm</b></td><td>સાડી બોર્ડર / બોક્સ</td><td>150 mm ઓફસેટ હાફ-ડ્રોપ</td></tr>
                        <tr><td><b>330 mm</b></td><td>દહાઓ હેડ સ્પેસિંગ</td><td>મલ્ટી-હેડ સ્ટાન્ડર્ડ શિફ્ટ</td></tr>
                        <tr><td><b>400 mm</b></td><td>જમ્બો ફ્રેમ</td><td>વાસ્તવિક એરિયા 390 mm (5mm સેફ્ટી)</td></tr>
                        <tr><td><b>500 / 600 mm</b></td><td>હેવી પલ્લુ / લહેંગા</td><td>ડબલ હેડ જમ્પ સાથે</td></tr>
                    </tbody>
                </table>
            </div>
        </div>

        <div class="callout callout-tip">
            <div class="callout-icon">💡</div>
            <div class="callout-content">
                <strong>માપ લેવાનો સુવર્ણ નિયમ:</strong>
                જ્યારે પણ ગ્રાહક ઇંચમાં સેમ્પલ આપે ત્યારે તેને 25.4 વડે ગુણીને જ EmCAD માં ડ્રોઇંગ શરૂ કરો. સાડીની લંબાઈ 3 મીટર હોય તો 3000 mm થાય, જેને 300 mm ના 10 સરખા ભાગમાં વહેંચી શકાય છે.
            </div>
        </div>
    </div>
    """

    
    
    sec_animations = """
    <div class="section-card" id="sec-simulations">
        <div class="section-header">
            <div class="section-title">
                <span>🎬</span> Section 2A: Interactive Stitching Simulation & Motion Graphics Studio
            </div>
            <span class="section-tag">લાઇવ મશીન સિમ્યુલેટર અને ૮ મોશન એનિમેશન્સ</span>
        </div>
        <p style="margin-bottom: 16px; font-size: 14px;">
            નવા પંચિંગ ડિઝાઇનર્સ અને વિદ્યાર્થીઓને મશીન કેવી રીતે ચાલે છે, જમ્પ કેવો દેખાય છે, લૂપિંગ (ફંદા) કેવી રીતે બને છે, 
            સિક્વિન અને ડબલ સ્ટેકિંગ કેવી રીતે લોક થાય છે, અને ઓરિજિન લોક કેમ જરૂરી છે તે સમજાવવા માટે નીચે 
            <b>અત્યાધુનિક લાઇવ કેનવાસ સિમ્યુલેટર (સાઉન્ડ અને સ્ક્રબર સાથે)</b> અને <b>૮ હાઇ-ડેફિનેશન એનિમેશન વિડીયો-પ્લેટ્સ</b> સામેલ કરવામાં આવી છે:
        </p>

        <!-- LIVE INTERACTIVE EMBROIDERY SIMULATOR -->
        <div class="sim-container">
            <div class="sim-header">
                <h3><span>🕹️</span> EmCAD 3D Multi-Device Embroidery Studio & Live Simulator</h3>
                <span class="sim-badge">REAL-TIME PHYSICAL NEEDLE ENGINE</span>
            </div>

            <!-- Controls Deck -->
            <div class="sim-controls">
                <select id="simScenario" class="sim-select" onchange="resetSim()">
                    <option value="jump">૧. ⚡ સ્ટીચિંગ vs જમ્પ & Auto-Trim</option>
                    <option value="looping">૨. ➰ લૂપિંગ / ચેનીલ ફંદા (3D Velvet Terry Loop)</option>
                    <option value="sequin_fish">૩. ✨ સિક્વિન (ટિકી) 3mm Fish-Scale & Fix 26</option>
                    <option value="sequin_stack">૪. 🌟 ડબલ સિક્વિન સ્ટેકિંગ (5mm + 3mm Stack)</option>
                    <option value="beads_taka">૫. 📿 બીડ્સ (Pearl 2.30mm & Cutdana 4.50mm)</option>
                    <option value="beads_curve">૬. 🌿 વળાંકવાળા પાથ પર બીડ્સ & કટદાણા ૯° ટિલ્ટ</option>
                    <option value="flower_cluster">૭. 🌸 ક્લસ્ટર ફ્લાવર (Pearl Center + Sequin Petals)</option>
                    <option value="paghdi">૮. 👑 પાઘડી (Paghdi F4 Column Satin Fill)</option>
                    <option value="origin">૯. 🎯 ઓરિજિન લોક DR 250 (Tie-in & Tie-off)</option>
                </select>

                <button class="sim-btn" onclick="togglePlaySim()" id="btnPlay">▶ Play</button>
                <button class="sim-btn sim-btn-secondary" onclick="stepSim(-1)">◀ -1 Step</button>
                <button class="sim-btn sim-btn-secondary" onclick="stepSim(1)">+1 Step ▶</button>
                <button class="sim-btn sim-btn-secondary" onclick="toggleSpeedSim()" id="btnSpeed">⚡ Speed: 1x</button>
                <button class="sim-btn sim-btn-secondary" onclick="resetSim()">🔄 Reset</button>
                <button class="sim-btn sim-btn-secondary" onclick="toggleSound()" id="btnSound">🔇 Sound: OFF</button>

                <select class="sim-select" onchange="onThreadColorChange(this.value)">
                    <option value="#EF4444">🧵 લાલ દોરો (Ruby Red)</option>
                    <option value="#F59E0B">🧵 સોનેરી જરી (Gold Zari)</option>
                    <option value="#10B981">🧵 લીલો દોરો (Emerald Green)</option>
                    <option value="#38BDF8">🧵 રોયલ બ્લુ (Royal Blue)</option>
                    <option value="#F8FAFC">🧵 શુદ્ધ સફેદ / સિલ્વર (White/Silver)</option>
                </select>
            </div>

            <!-- Timeline Scrubber -->
            <div class="sim-scrubber-box">
                <label>⏱️ સ્ટીચ ટાઇમલાઇન સ્ક્રબર:</label>
                <input type="range" id="simScrubber" min="0" max="140" value="0" class="sim-scrubber" oninput="onScrubSim(this.value)">
            </div>

            <!-- Canvas Viewport -->
            <div class="sim-canvas-wrapper">
                <canvas id="simCanvas" class="sim-canvas" width="960" height="420"></canvas>
            </div>

            <!-- Telemetry HUD -->
            <div class="sim-telemetry-grid">
                <div class="sim-hud-card">
                    <div class="sim-hud-label">મશીન સ્ટેટસ</div>
                    <div class="sim-hud-val" id="hudStatus" style="font-size: 11.5px; color:#F59E0B;">READY</div>
                </div>
                <div class="sim-hud-card">
                    <div class="sim-hud-label">સોય કો-ઓર્ડિનેટ્સ</div>
                    <div class="sim-hud-val" id="hudCoords">X=0 mm, Y=0 mm</div>
                </div>
                <div class="sim-hud-card">
                    <div class="sim-hud-label">ટાંકા કાઉન્ટ & પ્રોગ્રેસ</div>
                    <div class="sim-hud-val" id="hudStitchCount" style="color:#10B981;">0 TAKA (0%)</div>
                </div>
                <div class="sim-hud-card">
                    <div class="sim-hud-label">મશીન સ્પીડ (RPM)</div>
                    <div class="sim-hud-val" id="hudRpm">850 RPM</div>
                </div>
                <div class="sim-hud-card">
                    <div class="sim-hud-label">Z-સ્ટ્રોક પોઝિશન</div>
                    <div class="sim-hud-val" id="hudZStroke" style="color:#E2E8F0;">DOWN (PIERCING)</div>
                </div>
            </div>
        </div>

        <h3 style="color: var(--primary); margin: 36px 0 16px 0; font-size: 19px;">🎥 Complete 8 Motion Graphics & Visual Mechanics Guide</h3>

        <!-- Animation 1: Jump -->
        <div class="anim-card">
            <div class="anim-card-header">
                <h4><span>⚡</span> ૧. મશીન સ્ટીચિંગ vs જમ્પ (Stitch vs Jump Simulation)</h4>
                <span class="badge-code">Step 4 Jump Mechanics</span>
            </div>
            <div class="anim-container">
                <img src="emCad_organized_assets/anim_jump_stitching_simulation.gif" alt="Jump Stitching Simulation" loading="lazy">
            </div>
            <div class="anim-caption">
                <b>મહત્વપૂર્ણ સિદ્ધાંત:</b> લાલ ઘાટી લાઇન એટલે સોય કાપડની અંદર ઊતરીને ટાંકો પાડે છે. જ્યારે ડિઝાઇનના બે અલગ અલગ ભાગ વચ્ચે જવાનું હોય ત્યારે સોય ઊંચી રહે છે અને ફ્રેમ ઝડપથી ખસે છે જેને <b>વાદળી તૂટક લાઇન (Jump)</b> કહે છે. ૫ mm થી મોટો જમ્પ હોય ત્યારે કમ્પ્યુટર આપોઆપ કાતરથી દોરો કાપે છે (Auto-Trim).
            </div>
        </div>

        <!-- Animation 2: Looping (NEW) -->
        <div class="anim-card">
            <div class="anim-card-header">
                <h4><span>➰</span> ૨. લૂપિંગ / ચેનીલ ફંદા એમ્બ્રોઇડરી (Chenille / Terry Loop Mechanics)</h4>
                <span class="badge-code">Loop Height: 1.5 - 4.5mm</span>
            </div>
            <div class="anim-container">
                <img src="emCad_organized_assets/anim_looping_chain_stitch.gif" alt="Looping Chain Stitch Simulation" loading="lazy">
            </div>
            <div class="anim-caption">
                <b>લૂપિંગ પંચિંગ નિયમ:</b> સ્પેશિયલ પોચી સોય (Schmetz 120/19) કાપડમાં નીચે ઊતરે છે અને નીચેથી ૩૬૦° ફરતો લૂપર હૂક ઊનના દોરાને પકડીને ઉપર ૩.૦ mm ઊંચો લૂપ બનાવે છે. આનાથી કાપડ પર વેલ્વેટ/ટવેલ જેવો સોફ્ટ 3D પ્લશ ટેક્સચર બને છે. મશીન સ્પીડ ૪૦૦ થી ૬૦૦ RPM વચ્ચે કંટ્રોલ કરવી જરૂરી છે.
            </div>
        </div>

        <!-- Animation 3: Sequin Overlap -->
        <div class="anim-card">
            <div class="anim-card-header">
                <h4><span>✨</span> ૩. સિક્વિન (ટિકી) ફીડર ડ્રોપ અને Fix Type 26 ત્રિકોણ લોક</h4>
                <span class="badge-code">Fix Type 26 Triangle Lock</span>
            </div>
            <div class="anim-container">
                <img src="emCad_organized_assets/anim_sequin_overlap_lock.gif" alt="Sequin Overlap Lock Simulation" loading="lazy">
            </div>
            <div class="anim-caption">
                <b>સિક્વિન પંચિંગ નિયમ:</b> મશીનનું ફીડર ગોલ્ડન ટિકીને કાપડ પર નીચે મૂકે છે. સોય ટિકીના સેન્ટર કાણામાં ઊતરીને ૧૨૦° ના ખૂણે ૩ અલગ અલગ ટાંકા મારીને ત્રિકોણ લોક (Fix Type 26) બનાવે છે. દરેક નવી ટિકી અગાઉની ટિકી પર ૪૦% ઓવરલેપ થઈને માછલીની છાલ જેવો અદભુત લુક આપે છે.
            </div>
        </div>

        <!-- Animation 4: Sequin Double Stack (NEW) -->
        <div class="anim-card">
            <div class="anim-card-header">
                <h4><span>🌟</span> ૪. ડબલ સિક્વિન સ્ટેકિંગ (5mm Gold Base + 3mm Silver Top Stack)</h4>
                <span class="badge-code">Dual Device Concentric Lock</span>
            </div>
            <div class="anim-container">
                <img src="emCad_organized_assets/anim_sequin_double_stack.gif" alt="Sequin Double Stack Simulation" loading="lazy">
            </div>
            <div class="anim-caption">
                <b>ડબલ સ્ટેક નિયમ:</b> Chute A માંથી 5mm મોટી ગોલ્ડન ટિકી પડે છે અને તરત Chute B માંથી 3mm નાની સિલ્વર હોલોગ્રામ ટિકી તેની ઉપર સેન્ટરમાં પડે છે. એક જ નીડલ સ્ટ્રાઇક બંને ટિકીના સેન્ટર કાણામાંથી પસાર થઈને ૪-પોઇન્ટ સ્ટાર લોક મારી બંનેને એકસાથે મજબૂત રીતે જકડી લે છે. હાઇ-એન્ડ બ્રાઇડલ લહેંગા માટે ઉત્તમ.
            </div>
        </div>

        <!-- Animation 5: Beads Taka -->
        <div class="anim-card">
            <div class="anim-card-header">
                <h4><span>📿</span> ૫. બીડ્સ (મોતી & કટદાણા) ટાંકો અને ૯° રોટેશન</h4>
                <span class="badge-code">Alt + CapsLock 9° Tilt</span>
            </div>
            <div class="anim-container">
                <img src="emCad_organized_assets/anim_beads_taka_placement.gif" alt="Beads Taka Placement Simulation" loading="lazy">
            </div>
            <div class="anim-caption">
                <b>ટાંકો લંબાઈ સુવર્ણ નિયમ:</b> ગોળ મોતી (2.0 mm) માટે ટાંકો લંબાઈ ૨.૩૦ mm રાખવી. લાંબી કાચની નળી (Cutdana 4.0 mm) માટે ટાંકો ૪.૫૦ mm રાખવો (નળી કરતાં 0.5 mm મોટો). વળાંક પર કટદાણાને ૯ ડિગ્રીના સ્ટેપમાં ફેરવવા માટે <code>Alt + CapsLock</code> શોર્ટકટ કી વાપરવી.
            </div>
        </div>

        <!-- Animation 6: Beads Curved Contour (NEW) -->
        <div class="anim-card">
            <div class="anim-card-header">
                <h4><span>🌿</span> ૬. વળાંકવાળા પાથ પર બીડ્સ અને કટદાણા ૯° ટિલ્ટ</h4>
                <span class="badge-code">Continuous S-Curve Alignment</span>
            </div>
            <div class="anim-container">
                <img src="emCad_organized_assets/anim_beads_curved_contour.gif" alt="Beads Curved Contour Simulation" loading="lazy">
            </div>
            <div class="anim-caption">
                <b>કર્વ્ડ પાથ પ્રોટેક્શન:</b> ગળાની નેકલાઇન કે પાંદડીના એસ-કર્વ વળાંક પર જ્યારે કટદાણા ચાલતા હોય ત્યારે સોયની દિશા વળાંકના સ્પર્શક (Tangent) સાથે સતત ૯° ના સ્ટેપમાં ગોઠવાય છે. જો આ ખૂણો ખોટો હોય તો સોય કાચની નળી પર પડીને નળી તોડી નાખે છે!
            </div>
        </div>

        <!-- Animation 7: Paghdi -->
        <div class="anim-card">
            <div class="anim-card-header">
                <h4><span>👑</span> ૭. પાઘડી (Paghdi F4) કોલમ સિમેટ્રી સાટિન સ્ટીચિંગ</h4>
                <span class="badge-code">F4 Column Symmetry</span>
            </div>
            <div class="anim-container">
                <img src="emCad_organized_assets/anim_paghdi_column_stitching.gif" alt="Paghdi Column Stitching Simulation" loading="lazy">
            </div>
            <div class="anim-caption">
                <b>પાઘડી પંચિંગ પદ્ધતિ:</b> વાદળી રંગની બંને બાઉન્ડ્રી રેલ વચ્ચે પીળા સાટિન ટાંકા સમાંતર એંગલે ભરાય છે. ખૂણા માટે કીબોર્ડ પરથી <b>'D' (Square Corner Node)</b> અને વળાંક માટે <b>'O' (Smooth Curve Node)</b> વપરાય છે. પહોળાઈ ૧૧૦૦ (0.8 mm થી 1.1 mm) જળવાઈ રહે છે.
            </div>
        </div>

        <!-- Animation 8: Lock & Origin -->
        <div class="anim-card">
            <div class="anim-card-header">
                <h4><span>🔒</span> ૮. Tie-in લોક, ટાંકો, Tie-off લોક અને ઓરિજિન DR 250</h4>
                <span class="badge-code">DR 250 Origin Lock (0,0)</span>
            </div>
            <div class="anim-container">
                <img src="emCad_organized_assets/anim_lock_origin_dr250.gif" alt="Lock and Origin DR 250 Simulation" loading="lazy">
            </div>
            <div class="anim-caption">
                <b>પ્રોડક્શન સલામતી:</b> શરૂઆતમાં ૩ ટાંકા ગાંઠ (Tie-in), ડિઝાઇન પત્યા પછી ૪ ટાંકા પેક (Tie-off), કાતરથી દોરો કાપવો (Auto-Trim) અને અંતે <code>Ctrl + Home</code> આપી સોયને મશીન ઓરિજિન <b>DR 250 (X=0, Y=0)</b> પર પાછી પાર્ક કરવી જેથી ૨૫-હેડ મશીનમાં ક્યારેય ફ્રેમ હિટ ન થાય!
            </div>
        </div>
    </div>
    """

    sec_comparisons = """
    <div class="section-card" id="sec-comparisons">
        <div class="section-header">
            <div class="section-title">
                <span>⚡</span> Master Visual Comparison Showcase: Vector Drawing vs Real Embroidered Fabric
            </div>
            <span class="section-tag">કિસકો ક્યા કહા જાતા હૈ - સંપૂર્ણ સરખામણી ગેલેરી</span>
        </div>
        <p style="margin-bottom: 16px; font-size: 14px;">
            નવા પંચિંગ ડિઝાઇનર્સ અને ઓપરેટર્સ માટે સૌથી મોટો પ્રશ્ન એ હોય છે કે <b>"સોફ્ટવેરમાં દોરેલી વેક્ટર લાઇન મશીન પર કેવા પ્રકારની દેખાય છે અને કયા ભાગને શું કહેવાય છે?"</b><br/>
            નીચે <b>પાઘડી (Paghdi), સિક્વિન (Sequin), બીડ્સ (Beads), મિરરિંગ (Mirror), શેડિંગ ફ્લાવર (Shading Flower) અને કોર્ડિંગ (Cording)</b> ના ૬ હાઇ-ડેફિનેશન ડ્યુઅલ-પેનલ બોર્ડ્સ આપેલા છે, જેમાં ડાબી બાજુ કમ્પ્યુટર વેક્ટર પાથ અને જમણી બાજુ વાસ્તવિક મશીન સ્ટીચિંગ આપેલું છે:
        </p>

        <h3 style="color: var(--primary); margin: 24px 0 12px 0;">📊 Master Embroidery Techniques & Anatomy Comparison Table</h3>
        <table class="data-table">
            <thead>
                <tr>
                    <th style="width: 130px;">ટેકનિક / વર્ક</th>
                    <th style="width: 120px;">સોફ્ટવેર કમાન્ડ</th>
                    <th style="width: 170px;">વેક્ટર ડ્રોઇંગ શરીરરચના (CAD Anatomy)</th>
                    <th style="width: 160px;">મશીન પંચિંગ કોડ</th>
                    <th>વાસ્તવિક કાપડ દેખાવ (Real Stitched Fabric Look)</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><b>પાઘડી (Paghdi)</b></td>
                    <td><span class="badge-code">F4 Column Symmetry</span></td>
                    <td>મધ્ય અક્ષિસ (X=0), બાઉન્ડ્રી પાટા, Node 'D' (ચોરસ), Node 'O' (વળાંક), એંગલ લાઇન</td>
                    <td>1100 -> Enter (પહોળાઈ 0.8 - 1.1 mm)</td>
                    <td>સોનેરી જરીના ઉપસેલા ચળકતા સાટિન સ્ટીચ ટાંકા. વેલ, પાંદડી અને કેરીમાં વપરાય.</td>
                </tr>
                <tr>
                    <td><b>સિક્વિન (Sequin / ટિકી)</b></td>
                    <td><span class="badge-code">Object Property -> Sequin</span></td>
                    <td>ટિકી સર્કલ (2-5mm), સેન્ટર કાણું, Overlap Sew, 3-Point Tie Stitch</td>
                    <td>Fix Type 26 (ત્રિકોણ લોક)</td>
                    <td>માછલીની છાલ જેવી એકબીજા પર ચડેલી સોનેરી/રૂપેરી મેટાલિક ટિકી. ચમકદાર બોર્ડર લુક.</td>
                </tr>
                <tr>
                    <td><b>બીડ્સ (Beads / મોતી-કટદાણા)</b></td>
                    <td><span class="badge-code">Step 11 & 16 Beads</span></td>
                    <td>ગોળ મોતી ટ્રેક, 4mm કાચની નળી, Taka Spacing, Alt+CapsLock 9° એંગલ</td>
                    <td>Taka = 2.15mm (મોતી), 4.5mm (નળી)</td>
                    <td>હાથવણાટ જેવો લક્ઝરી લુક. વેલ્વેટ પર શુદ્ધ સફેદ મોતી અને સોનેરી નળીઓનું ભવ્ય કામ.</td>
                </tr>
                <tr>
                    <td><b>મિરરિંગ (Mirror 'R')</b></td>
                    <td><span class="badge-code">'R' Key -> 2-Click</span></td>
                    <td>મધ્ય અરીસાની ધરી લાઇન (Center Axis), ડાબો મૂળ ભાગ, જમણો ૧૦૦% સરખો ભાગ</td>
                    <td>Center Lock / Flip Axis</td>
                    <td>નેકલાઇન, ગળા અને સાડીના પાલવમાં બંને બાજુ આબેહૂબ સપ્રમાણ બેલેન્સ ડિઝાઇન.</td>
                </tr>
                <tr>
                    <td><b>શેડિંગ (Flower Shading)</b></td>
                    <td><span class="badge-code">F3 Tatami + Keys 1-6</span></td>
                    <td>Needle 1 (Base), Needle 2 (Mid), Needle 3 (Tip), 90° Perpendicular Fill, Florentine</td>
                    <td>90° Angle Cross & Step Blend</td>
                    <td>ઘાટા લાલથી ગુલાબી અને સફેદ રંગમાં વણાયેલી કળાત્મક પાંખડીઓ. 3D વેવ નેચરલ લુક.</td>
                </tr>
                <tr>
                    <td><b>કોર્ડિંગ (F12 Dori Work)</b></td>
                    <td><span class="badge-code">F12 Cording Tool</span></td>
                    <td>સેન્ટ્રલ જાડી દોરી (Core Cord), બંને બાજુ પકડ ઝિગઝેગ ટાંકા (Zigzag Tack)</td>
                    <td>Angle = 50, 35, 21; Times = 2</td>
                    <td>દોરી કાપ્યા વગર કાપડ પર ઉપસેલી 3D જરી દોરી. હેવી લગ્ન-પોશાક અને કુરતી નેક વર્ક.</td>
                </tr>
                <tr>
                    <td><b>લૂપિંગ (Looping / Chenille)</b></td>
                    <td><span class="badge-code">Chenille Loop Mode</span></td>
                    <td>હોલો સોય (120/19), લૂપર હૂક ૩૬૦°, લૂપ હાઇટ ૧.૫ - ૪.૫ mm, ઊન/એક્રેલિક ફ્લફી દોરો</td>
                    <td>Loop Height = 3.0mm; RPM = 500</td>
                    <td>વેલ્વેટ/ટવેલ જેવો સોફ્ટ 3D પ્લશ ટેક્સચર. રોયલ બ્લુ વેલ્વેટ પર ગોલ્ડન લૂપ કાર્પેટ.</td>
                </tr>
                <tr>
                    <td><b>સ્ટેક્ડ સિક્વિન & બીડ્સ</b></td>
                    <td><span class="badge-code">Dual Device + Radial Array</span></td>
                    <td>૫mm બેઝ ટિકી + ૩mm ટોપ ટિકી સ્ટેક, કટદાણા ૪.૫૦mm રેડિયલ એરે, ૯° એંગલ ટિલ્ટ</td>
                    <td>Concentric Single Lock; Taka = 4.5mm</td>
                    <td>કુતૂર બ્રાઇડલ લહેંગા જેવો ભવ્ય લક્ઝરી 3D લુક. હોલોગ્રાફિક શાઈન અને ગ્લાસ રિફ્લેક્શન.</td>
                </tr>
            </tbody>
        </table>

        <!-- Visual Comparison Cards 1 to 6 -->
        """ + comparison_card(
            "69_Compare_Paghdi_Vector_Drawing_vs_Real_Satin_Stitch.jpg",
            "૧. પાઘડી (Paghdi / Column Symmetry F4) - સંપૂર્ણ સરખામણી",
            "EmCAD Vector Column Nodes & Angle Lines vs Real Embroidered Satin Stitch on Silk",
            ['<b>Centerline Axis (મધ્ય અક્ષિસ રેખા - X=0):</b> કૉલમની બરાબર વચ્ચેથી પસાર થતી રેખા, જેની બંને બાજુ સમાન અંતરે સાટિન સ્ટીચના પોઇન્ટ્સ પડે છે.', '<b>Boundary Rails (બાઉન્ડ્રી પાટા / ડાબી-જમણી રેખા):</b> વાદળી રંગની બે કિનારી રેખાઓ જે સાટિન સ્ટીચની બહારની સીમા અને પહોળાઈ નક્કી કરે છે.', "<b>Node 'D' (લાલ ચોરસ બોક્સ - Sharp Corner Node):</b> ખૂણો પાડવા માટે વપરાતો તીક્ષ્ણ પોઇન્ટ (કીબોર્ડ 'D' કી). આનાથી પાઘડીના છેડા પર ચોખ્ખી અણી બને છે.", "<b>Node 'O' (લીલું ગોળ સર્કલ - Smooth Curve Node):</b> વળાંકવાળા આકાર માટે વપરાતો સ્મૂથ નોડ (કીબોર્ડ 'O' કી). આનાથી પાંદડીમાં ક્યાંય ખામી વગરનો ગોળ વળાંક આવે છે.", '<b>Satin Angle Lines (પીળી સ્ટીચ લાઇન - Stitch Angle):</b> સોય કઈ દિશામાં દોરો ચલાવશે તે દર્શાવતી સમાંતર રેખાઓ. ખૂણા પ્રમાણે આ રેખાઓ આપોઆપ વળે છે.', '<b>Column Width (કૉલમ પહોળાઈ):</b> સ્ટાન્ડર્ડ પહોળાઈ ૧૧૦૦ (કીબોર્ડ 1100 -> Enter = 0.8 mm થી 1.1 mm). 0.8 mm થી ઓછી પહોળાઈમાં સોય દોરો કાપી નાખે છે.', '<b>Short Stitches = 0.5 mm (શોર્ટ સ્ટીચ સિક્યુરિટી):</b> તીવ્ર વળાંક પર અંદરની બાજુ ટાંકા ગૂંચવાઈ ન જાય તે માટે ઓટોમેટિક શોર્ટ સ્ટીચ ફિલ્ટર.', '<b>Real Fabric Result (વાસ્તવિક કાપડ પરિણામ):</b> જમણી બાજુ રોયલ બ્લુ સિલ્ક ફેબ્રિક પર સોનેરી જરીના ઉપસેલા (3D Embossed) ચળકતા સાટિન સ્ટીચ ટાંકાનું ઉત્કૃષ્ટ પરિણામ.']
        ) + """

        """ + comparison_card(
            "70_Compare_Sequin_Vector_Drawing_vs_Real_Embroidery.jpg",
            "૨. સિક્વિન (Sequin / ટિકી વર્ક) - સંપૂર્ણ સરખામણી",
            "EmCAD Sequin Drop Path & Fix Type 26 vs Real Overlapping Metallic Sequins on Georgette",
            ['<b>Sequin Metallic Disc (ટિકી સર્કલ):</b> સોનેરી કે સિલ્વર મેટાલિક ચમકતી પતરી, સામાન્ય વ્યાસ 2.0 mm, 3.0 mm અથવા 5.0 mm.', '<b>Center Needle Hole (મધ્ય સોયનું કાણું):</b> ટિકીના કેન્દ્રમાં આવેલું કાણું, જ્યાં સોય નીચે ઊતરીને ટિકીને દોરા વડે કાપડ સાથે જકડી રાખે છે.', '<b>Overlap Sew (માછલીની છાલ જેવો ઓવરલેપ લુક):</b> સિક્વિન ૪૦% થી ૫૦% એકબીજા પર ચડીને બેસે છે જેથી વચ્ચેનું બેઝ કાપડ બિલકુલ દેખાતું નથી.', '<b>Fix Type 26 (3-Point Triangle Lock / તીરછા-ત્રિકોણ લોક ટાંકો):</b> કાણામાંથી ૩ તરફ ૧૨૦° ના ખૂણે દોરાના ટાંકા મારીને ત્રિકોણ આકારે પેક કરવામાં આવે છે જેથી ધોવાયા પછી પણ ટિકી ઊખડે નહીં.', '<b>Drop Sequin Dir (ટિકી પડવાની દિશા):</b> મશીન હેડ કઈ દિશામાં આગળ વધી રહ્યું છે (Any, 0°, 90°) તે મુજબ ટિકી આપોઆપ એકબીજાની પાછળ ડ્રોપ થાય છે.', '<b>Expand to Fit vs Contract to Fit:</b> ડિઝાઇનની આઉટલાઇનથી ટિકી બહાર સુધી ફેલાવવી (Expand) કે અંદર સંકોચાઈને સેફ માર્જિન રાખવું (Contract).', '<b>Tie Stitch (લોક સ્ટીચ):</b> સિક્વિન પટ્ટી શરૂ થતાં અને પૂરી થતાં ૩-૪ નાના ટાંકા મારીને દોરો ગાંઠવામાં આવે છે.', '<b>Real Fabric Result (વાસ્તવિક કાપડ પરિણામ):</b> જમણી બાજુ એમેરાલ્ડ ગ્રીન જ્યોર્જેટ કાપડ પર ગોલ્ડ અને સિલ્વર મેટાલિક ટિકીનું આબેહૂબ માછલીની છાલ જેવું હાઈ-ફિનિશિંગ એમ્બ્રોઇડરી.']
        ) + """

        """ + comparison_card(
            "71_Compare_Beads_Vector_Drawing_vs_Real_Embroidery.jpg",
            "૩. બીડ્સ (Beads / મોતી અને કટદાણા) - સંપૂર્ણ સરખામણી",
            "EmCAD Beads Spacing & Taka Table vs Real Glass Pearls & Cutdana Beads on Velvet",
            ['<b>Round Pearl Beads (Beads A - ગોળ મોતી):</b> સફેદ/ક્રીમ ગોળ મોતી (1.7 mm, 2.0 mm, 2.5 mm). સ્ટાન્ડર્ડ મશીન ટાંકો = 2.15 mm થી 2.30 mm.', '<b>Cutdana Bugle Pipe (Beads B - કાચની નળી / કટદાણા):</b> 4.0 mm લાંબી હેક્સાગોનલ કાચની નળી. મશીન ટાંકો લંબાઈ = 4.50 mm (નળી કરતાં 0.5 mm વધુ).', '<b>Taka Distance (ટાંકાનું ચોક્કસ અંતર):</b> સોયના બે પંચ વચ્ચેનું અંતર. જો ટાંકો નળી કરતાં નાનો હશે તો સોય કાચ સાથે અથડાઈને તૂટી જશે અને મશીન બંધ પડશે.', '<b>Alt + CapsLock (૯° એંગલ રોટેશન):</b> કટદાણાની નળીને ડિઝાઇનની દિશા મુજબ ૯ ડિગ્રીના સ્ટેપમાં ત્રાંસી ફેરવીને બેસાડવાની શોર્ટકટ કી.', '<b>Break Down (Alt+Y Cut / Alt+B Split):</b> ખૂણા પર બીડ્સ લાઇનને અલગ કરી સોય ફ્રી કરવા માટે Arrange -> Break Down કમાન્ડ.', '<b>Fix Adjust (Ctrl + A -> Fix Adjust):</b> પંચિંગ પૂર્ણ થયા પછી ઓવરલેપિંગ કાણાં અને ડબલ બીડ્સ ફિલ્ટર કરી કાઢી નાખવાનું ટૂલ.', '<b>Short Stitches = 0.5 mm સિક્યુરિટી:</b> ટર્નિંગ પોઇન્ટ પર સોય કાચની નળીને અડ્યા વગર સલામત રીતે બહાર નીકળી જાય તે માટે.', '<b>Real Fabric Result (વાસ્તવિક કાપડ પરિણામ):</b> જમણી બાજુ મરૂન રોયલ વેલ્વેટ ફેબ્રિક પર હાથવણાટ જેવી ઉત્કૃષ્ટ ફિનિશિંગ સાથે ગોલ્ડન કટદાણા અને શુદ્ધ સફેદ મોતીનું કળાત્મક સંયોજન.']
        ) + """

        """ + comparison_card(
            "72_Compare_Mirror_Vector_Drawing_vs_Real_Embroidery.jpg",
            "૪. મિરરિંગ (Mirror 'R' Key) - સંપૂર્ણ સરખામણી",
            "EmCAD 2-Click Center Mirror Axis vs Real Symmetrical Embroidered Saree Motif",
            ["<b>Center Mirror Axis Line (મધ્ય અરીસાની ધરી રેખા):</b> ડિઝાઇન સિલેક્ટ કરી 'R' દબાવીને જે લાલ રેખા દોરવામાં આવે છે તે મિરરિંગની મુખ્ય ધરી છે.", '<b>Original Half (મૂળ અડધો ભાગ):</b> ડાબી બાજુ દોરેલું પાન, કેરી કે બુટ્ટો. ડિઝાઇનરને માત્ર અડધો જ ભાગ મહેનત કરીને દોરવો પડે છે.', '<b>Mirrored Duplicate (સામેનું ૧૦૦% આબેહૂબ પ્રતિબિંબ):</b> એક્સિસની જમણી બાજુ કમ્પ્યુટર આપોઆપ પેદા કરતો સામસામો એકસરખો આકાર.', '<b>Click 1 (Start of Axis) & Click 2 (End of Axis):</b> માઉસ વડે બે ક્લિક આપી ઊભી અક્ષિસ (ડાબે-જમણે ફ્લિપ) કે આડી અક્ષિસ (ઉપર-નીચે ફ્લિપ) નક્કી થાય છે.', '<b>Step 15 સાડી નિયમ (400 mm એરિયા):</b> ૪૦૦ mm ના મશીન એરિયામાં પાલવ માટે ૧૬૦ mm સેન્ટર પર પલ્લું મિરર લોક કરવામાં આવે છે.', '<b>Symmetry Balance (સપ્રમાણ સંતુલન):</b> બંને બાજુની ઘનતા અને સ્ટીચ કાઉન્ટ બરાબર સરખા રહે છે જેથી કાપડ એક બાજુ ખેંચાતું નથી.', '<b>Real Fabric Result (વાસ્તવિક કાપડ પરિણામ):</b> જમણી બાજુ પિંક રો સિલ્ક ફેબ્રિક પર બ્લાઉઝ કે ડ્રેસના ગળાની બંને બાજુ સોનેરી જરીના બે સામસામે આબેહૂબ અરીસા જેવા પાંદડી-મોટીફનું પરિણામ.']
        ) + """

        """ + comparison_card(
            "73_Compare_Shading_Flower_Vector_Drawing_vs_Real_Embroidery.jpg",
            "૫. શેડિંગ ફ્લાવર (Shading Flower & Tatami Fill) - સંપૂર્ણ સરખામણી",
            "EmCAD 90° Perpendicular Fill & Color Sequence vs Real Gradient Embroidered Flower",
            ['<b>Needle 1: Dark Red Base Layer (તળિયું):</b> પાંખડીના નીચેના ભાગમાં ઘાટો લાલ રંગ જે ફૂલની ઊંડાઈ અને પડછાયો (Shadow) દર્શાવે છે.', '<b>Needle 2: Pink Mid-Tone Layer (વચ્ચેનો ભાગ):</b> મધ્યમાં ગુલાબી રંગ જે નીચેના ઘાટા લાલ સાથે ૨ થી ૩ mm અંદરોઅંદર ભળી જાય છે.', '<b>Needle 3: Ivory / White Tip (ઉપરની કિનારી):</b> પાંખડીની ટોચ પર આછો સફેદ/ક્રીમ રંગ જે પ્રકાશનો ચમકારો (Highlight) ઊભો કરે છે.', '<b>Perpendicular 90° Tatami Fill (કાટખૂણે છેદતી તતામી):</b> સામાન્ય તતામી કરતાં ૯૦ ડિગ્રી કાટખૂણે ટાંકા છેદે છે જેથી સૂર્યપ્રકાશમાં ડબલ-શેડ ચમક પેદા થાય છે.', '<b>Florentine Effect (મોજા જેવો વળાંક):</b> પાંખડીમાં સીધી લીટીને બદલે વળાંકવાળી એંગલ લાઇન વડે પાણીના મોજા જેવો લુક (Curved Angle Fill).', '<b>Color Sequence Keys (Keys 1 to 9):</b> કીબોર્ડ 1 થી 9 કી વડે ૯-સોય મશીનના દોરાના કલર સ્ટેપ-બાય-સ્ટેપ બદલવામાં આવે છે.', '<b>Real Fabric Result (વાસ્તવિક કાપડ પરિણામ):</b> જમણી બાજુ ક્રીમ સિલ્ક કાપડ પર ઘાટા લાલથી ગુલાબી અને સફેદ રંગમાં વણાયેલી કળાત્મક પાંખડીઓનું કુદરતી કલર-શેડિંગ.']
        ) + """

        """ + comparison_card(
            "74_Compare_Cording_Dori_Vector_Drawing_vs_Real_Embroidery.jpg",
            "૬. કોર્ડિંગ (Cording F12 દોરી વર્ક) - સંપૂર્ણ સરખામણી",
            "EmCAD Core Cord & Zigzag Tack Stitch vs Real Raised 3D Dori Embroidery on Velvet",
            ['<b>Core Cord (મુખ્ય જાડી દોરી - પીળી સેન્ટ્રલ દોરી):</b> સોનેરી જરી કે સિલ્કની જાડી દોરી જે મશીનના ગાઇડ પાઇપમાંથી કાપડની સપાટી પર સતત પથરાય છે.', '<b>Needle Zigzag Tack Stitch (ઝિગઝેગ પકડ ટાંકો - લાલ ટાંકા):</b> સોય દોરીને કાપ્યા વગર તેની બંને બાજુ ડાબે-જમણે કૂદીને ઝિગઝેગ સ્ટીચ વડે કાપડ સાથે જકડે છે.', '<b>F12 Cording Parameter: Angle = 50, 35, 21; Times = 2:</b> વળાંક પર સોયનો એંગલ ૫૦°, ૩૫°, ૨૧° રહે છે અને દોરી બમણી મજબૂતાઈથી ટંકાય છે.', '<b>Lead-In Start Lock (શરૂઆતનો પેક ટાંકો):</b> દોરી શરૂ થતાં ૨ mm આગળથી દોરાનો રન સ્ટીચ ચલાવીને દોરીનો છેડો કાપડમાં દબાવવો.', '<b>Lead-Out End Lock (છેલ્લા છેડાનો ટાઇ-ઓફ):</b> દોરી પતે ત્યારે સોય ૩-૪ ટાંકા મારીને દોરો પેક કરે છે જેથી ધોવાયા પછી દોરીનો છેડો છૂટો ન પડે.', '<b>Island Cording (આઇલેન્ડ દોરી પદ્ધતિ):</b> મોટીફની અંદરનો ભાગ ખાલી રાખી માત્ર બહારની કિનારી પર જ જાડી દોરી ચલાવીને 3D આઉટલાઇન આપવી.', '<b>Real Fabric Result (વાસ્તવિક કાપડ પરિણામ):</b> જમણી બાજુ નેવી બ્લુ રોયલ વેલ્વેટ પર ઉપસેલી સોનેરી દોરીનું ઉત્કૃષ્ટ 3D એમ્બોસ્ડ હેવી લગ્ન-પોશાક વર્ક.']
        ) + """

        """ + comparison_card(
            "75_Compare_Looping_Vector_Drawing_vs_Real_Embroidery.jpg",
            "૭. લૂપિંગ (Looping / Chenille / ફંદા એમ્બ્રોઇડરી) - સંપૂર્ણ સરખામણી",
            "EmCAD Vector Loop Path & Height Settings vs Real 3D Velvet Chenille Garment",
            ['<b>Hollow Chenille Needle (પોચી હોલો સોય - 120/19):</b> સામાન્ય સોય કરતાં પોચી અને જાડી સોય જેની અંદરથી ઊન કે એક્રેલિકનો ફ્લફી દોરો પસાર થાય છે.', '<b>Rotating Looper Hook (લૂપર હૂક ૩૬૦°):</b> કાપડની નીચે આવેલો સ્પેશિયલ હૂક જે સોય નીચે ઊતરે ત્યારે દોરાને પકડીને લૂપ વણી લે છે.', '<b>Loop Height Setting (૧.૫ mm થી ૪.૫ mm):</b> સોફ્ટવેરમાં લૂપની ઊંચાઈ નક્કી થાય છે. ૩.૦ mm લૂપ હાઇટથી રોયલ પ્લશ ટેક્સચર મળે છે.', '<b>Loop Density & Underlay:</b> લૂપિંગ નીચે હળવો રનિંગ સ્ટીચ અંડરલે આપવો ફરજિયાત છે જેથી કાપડ ખેંચાઈને સંકોચાઈ ન જાય.', '<b>Reverse 4-Stitch Lock (ચેઈન રિવર્સ લૉક):</b> લૂપ પૂરું થતાં ૪ નાના ટાંકા રિવર્સ મારીને લૂપ બાંધવો પડે છે જેથી દોરો ખેંચાતાં ખુલી ન જાય.', '<b>Speed Limit (૪૦૦-૬૦૦ RPM):</b> લૂપિંગ મશીનને ૬૦૦ RPM થી વધુ સ્પીડે ચલાવવું નહીં, નહીંતર લૂપ તૂટી જાય છે.', '<b>Real Fabric Result (વાસ્તવિક કાપડ પરિણામ):</b> જમણી બાજુ રોયલ નેવી બ્લુ વેલ્વેટ પર ગોલ્ડન અને ક્રીમ ઊનના દોરાથી બનેલું આબેહૂબ મોસ/ચેનીલ 3D એમ્બ્રોઇડરી.']
        ) + """

        """ + comparison_card(
            "76_Compare_Stacked_Sequin_Beads_Vector_vs_Real.jpg",
            "૮. સ્ટેક્ડ સિક્વિન & બીડ્સ (Stacked Sequins + Cutdana Cluster) - સંપૂર્ણ સરખામણી",
            "EmCAD Dual Sequin Drop + Bugle Bead Radiation vs Real Bridal Haute-Couture",
            ['<b>Dual Sequin Drop (Device A 5mm + Device B 3mm):</b> નીચે ૫mm મોટી ગોલ્ડન બેઝ ટિકી અને ઉપર ૩mm નાની સિલ્વર હોલોગ્રાફિક ટિકી.', '<b>Concentric Center Lock:</b> બંને ટિકીના સેન્ટર કાણામાંથી ૧ જ સોય ઊતરીને ૪-પોઇન્ટ સ્ટાર લૉક મારે છે.', '<b>Cutdana Radial Array (૪.૫૦ mm ટાંકો):</b> ફૂલની આસપાસ સૂર્યના કિરણોની જેમ ગોઠવાયેલી કાચની નળીઓ, ટાંકો ૪.૫૦ mm રાખવો.', '<b>Alt + CapsLock ૯° ટેન્જન્ટ એંગલ:</b> ગોળાકારમાં ફરતી વખતે કટદાણાની નળીઓ સોય સામે સીધી ૯૦° એંગલે ગોઠવાય છે જેથી કાચ તૂટતો નથી.', '<b>Pearl Halo Ring (૨.૩૦ mm મોતી):</b> વચ્ચે ૬mm મોતી અને ફરતે ૨mm નાના મોતીની રીંગ.', '<b>Real Fabric Result (વાસ્તવિક કાપડ પરિણામ):</b> જમણી બાજુ મરૂન સિલ્ક નેટ ફેબ્રિક પર લક્ઝરી ઇન્ડિયન બ્રાઇડલ હેવી એમ્બ્રોઇડરી, સ્ટેક્ડ ટિકી અને ચમકતા કટદાણા.']
        ) + """
    </div>
    """

    sec3 = """
    <div class="section-card" id="sec-drawing">
        <div class="section-header">
            <div class="section-title">
                <span>✏️</span> Section 3: Step 1 & Step 2: Vector Drawing & Basic Geometry
            </div>
            <span class="section-tag">ડ્રોઇંગ અને શેપ નિર્માણ</span>
        </div>
        <p style="margin-bottom: 16px;">
            કોઈપણ પંચિંગનું પહેલું પગથિયું સચોટ વેક્ટર ડ્રોઇંગ છે. જો ડ્રોઇંગમાં પોઇન્ટ્સ ખોટા હશે તો સ્ટીચિંગ વખતે કાપડ ખેંચાશે અને સોય તૂટશે.
        </p>

        <div class="image-gallery">
            """ + img_card("07_Step1_Drawing_Shapes_Mirror.jpg", "Step 1: બેઝિક શેપ્સ (A, B, C, D) અને મિરરિંગ 'R'", "પાંદડી, પાંખડી, ટીપું, સર્કલ ડ્રોઇંગ અને ૨-ક્લિક મિરર એક્સિસ") + """
            """ + img_card("08_Step2_Run_Flower_Circle_Divide.jpg", "Step 2: રન સ્ટીચ, ફ્લાવર સર્કલ અને સ્ટેપ કોપી", "ડિવાઇડ 'B', વેલ્ડ 'J' અને Alt + Right Arrow સ્ટેપ કોપી") + """
        </div>


        """ + comparison_card(
            "72_Compare_Mirror_Vector_Drawing_vs_Real_Embroidery.jpg",
            "મિરરિંગ સરખામણી: વેક્ટર ૨-ક્લિક એક્સિસ vs વાસ્તવિક સપ્રમાણ એમ્બ્રોઇડરી",
            "EmCAD 'R' Key Center Axis vs Real Symmetrical Motif on Saree Fabric",
            ["<b>Center Mirror Axis Line (મધ્ય અરીસાની ધરી રેખા):</b> ડિઝાઇન સિલેક્ટ કરી 'R' દબાવીને જે લાલ રેખા દોરવામાં આવે છે તે મિરરિંગની મુખ્ય ધરી છે.", '<b>Original Half (મૂળ અડધો ભાગ):</b> ડાબી બાજુ દોરેલું પાન, કેરી કે બુટ્ટો. ડિઝાઇનરને માત્ર અડધો જ ભાગ મહેનત કરીને દોરવો પડે છે.', '<b>Mirrored Duplicate (સામેનું ૧૦૦% આબેહૂબ પ્રતિબિંબ):</b> એક્સિસની જમણી બાજુ કમ્પ્યુટર આપોઆપ પેદા કરતો સામસામો એકસરખો આકાર.', '<b>Click 1 (Start of Axis) & Click 2 (End of Axis):</b> માઉસ વડે બે ક્લિક આપી ઊભી અક્ષિસ (ડાબે-જમણે ફ્લિપ) કે આડી અક્ષિસ (ઉપર-નીચે ફ્લિપ) નક્કી થાય છે.', '<b>Step 15 સાડી નિયમ (400 mm એરિયા):</b> ૪૦૦ mm ના મશીન એરિયામાં પાલવ માટે ૧૬૦ mm સેન્ટર પર પલ્લું મિરર લોક કરવામાં આવે છે.', '<b>Symmetry Balance (સપ્રમાણ સંતુલન):</b> બંને બાજુની ઘનતા અને સ્ટીચ કાઉન્ટ બરાબર સરખા રહે છે જેથી કાપડ એક બાજુ ખેંચાતું નથી.', '<b>Real Fabric Result (વાસ્તવિક કાપડ પરિણામ):</b> જમણી બાજુ પિંક રો સિલ્ક ફેબ્રિક પર બ્લાઉઝ કે ડ્રેસના ગળાની બંને બાજુ સોનેરી જરીના બે સામસામે આબેહૂબ અરીસા જેવા પાંદડી-મોટીફનું પરિણામ.']
        ) + """

        <table class="data-table">
            <thead><tr><th>આકાર (Shape)</th><th>દોરવાની સાચી રીત અને પંચિંગ ટિપ્સ</th></tr></thead>
            <tbody>
                <tr><td><b>Shape A (Leaf / પાંદડી)</b></td><td>બે પોઇન્ટ વચ્ચે વળાંક આપી તીક્ષ્ણ ખૂણો બનાવો. ડાબી બાજુ રાઉન્ડ પોઇન્ટ 'O' અને છેડે સ્ક્વેર પોઇન્ટ 'D'.</td></tr>
                <tr><td><b>Shape B (Petal / પાંખડી)</b></td><td>ઉપરથી ગોળાકાર અને નીચેથી સાંકડી. મધ્યમાં એંગલ લાઇન ૪૫ ડિગ્રી રાખવી.</td></tr>
                <tr><td><b>Shape C (Tear / ટીપું)</b></td><td>પાણીના ટીપા જેવો આકાર. નીચે મોટો વળાંક, ઉપર એક જ નોડ સ્ક્વેર.</td></tr>
                <tr><td><b>Shape D (Circle / વર્તુળ)</b></td><td>૪ પોઇન્ટ વડે પરફેક્ટ વર્તુળ. બરાબર ૯૦-૯૦ ડિગ્રી પર પોઇન્ટ્સ મૂકવા.</td></tr>
                <tr><td><b>Keri / Paisley (કેરી)</b></td><td>ભારતીય ડિઝાઇનની જાન. માથાનો ભાગ ગોળ, પૂંછડીનો ભાગ વળેલો. બે અલગ અલગ ભાગમાં દોરીને 'J' વડે Weld કરવું.</td></tr>
            </tbody>
        </table>

        <div class="callout callout-tip">
            <div class="callout-icon">💡</div>
            <div class="callout-content">
                <strong>મિરરિંગ (Mirroring) ની શોર્ટકટ ટ્રીક:</strong>
                ઓબ્જેક્ટ સિલેક્ટ કરી <b>'R'</b> દબાવો. સ્ક્રીન પર બે જગ્યાએ ક્લિક કરીને મિરર એક્સિસ નક્કી કરો. જો આડી અરીસા જેવી નકલ કરવી હોય તો બે આડી ક્લિક આપો, ઊભી નકલ કરવી હોય તો બે ઊભી ક્લિક આપો. <b>Step Copy માટે:</b> <code>Alt + Right Arrow</code> થી ઓબ્જેક્ટ આપોઆપ આપેલા માપ પ્રમાણે બાજુમાં કોપી થશે.
            </div>
        </div>
    </div>
    """

    sec4 = """
    <div class="section-card" id="sec-paghdi">
        <div class="section-header">
            <div class="section-title">
                <span>👑</span> Section 4: Step 3: Paghdi Making & Column Symmetry (F4 vs F2)
            </div>
            <span class="section-tag">પાગડી નિર્માણ F4 અને F2</span>
        </div>
        <p style="margin-bottom: 16px;">
            <b>પાઘડી (Paghdi / Column Symmetry)</b> એ સુરત એમ્બ્રોઇડરી ઉદ્યોગનો સૌથી લોકપ્રિય ટાંકો છે. 
            દરેક વેલ, પાંદડી, બોર્ડર અને ગળામાં પાઘડીનો ઉપયોગ થાય છે. EmCAD માં F4 થી કોલમ સિમેટ્રી બને છે.
        </p>

        <div class="image-gallery">
            """ + img_card("09_Step3_Paghdi_Column_F4_Basics.jpg", "Step 3: F4 પાઘડી બેઝિક્સ", "કોલમ સિમેટ્રી, એંગલ પોઇન્ટ્સ અને ૧૧૦૦ સ્ટાન્ડર્ડ પહોળાઈ") + """
            """ + img_card("10_Step3_Paghdi_Square_Spacing_Mirror.jpg", "Step 3: સ્ક્વેર પોઇન્ટ 'D' અને સ્પેસિંગ", "ખૂણા માટે 'D', વળાંક માટે 'O' અને સ્પેસિંગ >= 0.8 mm") + """
            """ + img_card("11_Step3_Paghdi_F2_Asymmetric_Method.jpg", "Step 3: F2 અનસિમેટ્રિક પાઘડી", "બંને બાજુ અલગ વળાંક અને પોઇન્ટ પેરિંગ પદ્ધતિ") + """
            """ + img_card("12_Step3_F6_Parallel_Run_Length.jpg", "Step 3: F6 ઇનપુટ પેરેલલ પટ્ટી", "સ્ટીચ લંબાઈ અને સમાંતર એંગલ લાઇન સેટિંગ") + """
            """ + img_card("68_Step3_Paghdi_Landscape_Original.jpg", "Step 3: પાઘડી માસ્ટર ચાર્ટ", "ઓરિજિનલ વર્કશોપ રેફરન્સ નોટ્સ અને પૂર્ણ આકૃતિ") + """
        </div>


        """ + comparison_card(
            "69_Compare_Paghdi_Vector_Drawing_vs_Real_Satin_Stitch.jpg",
            "પાઘડી સરખામણી: F4 કોલમ સિમેટ્રી નોડ્સ vs વાસ્તવિક સાટિન સ્ટીચ વર્ક",
            "EmCAD Vector Column Nodes vs Real Embroidered Satin Stitch on Silk",
            ['<b>Centerline Axis (મધ્ય અક્ષિસ રેખા - X=0):</b> કૉલમની બરાબર વચ્ચેથી પસાર થતી રેખા, જેની બંને બાજુ સમાન અંતરે સાટિન સ્ટીચના પોઇન્ટ્સ પડે છે.', '<b>Boundary Rails (બાઉન્ડ્રી પાટા / ડાબી-જમણી રેખા):</b> વાદળી રંગની બે કિનારી રેખાઓ જે સાટિન સ્ટીચની બહારની સીમા અને પહોળાઈ નક્કી કરે છે.', "<b>Node 'D' (લાલ ચોરસ બોક્સ - Sharp Corner Node):</b> ખૂણો પાડવા માટે વપરાતો તીક્ષ્ણ પોઇન્ટ (કીબોર્ડ 'D' કી). આનાથી પાઘડીના છેડા પર ચોખ્ખી અણી બને છે.", "<b>Node 'O' (લીલું ગોળ સર્કલ - Smooth Curve Node):</b> વળાંકવાળા આકાર માટે વપરાતો સ્મૂથ નોડ (કીબોર્ડ 'O' કી). આનાથી પાંદડીમાં ક્યાંય ખામી વગરનો ગોળ વળાંક આવે છે.", '<b>Satin Angle Lines (પીળી સ્ટીચ લાઇન - Stitch Angle):</b> સોય કઈ દિશામાં દોરો ચલાવશે તે દર્શાવતી સમાંતર રેખાઓ. ખૂણા પ્રમાણે આ રેખાઓ આપોઆપ વળે છે.', '<b>Column Width (કૉલમ પહોળાઈ):</b> સ્ટાન્ડર્ડ પહોળાઈ ૧૧૦૦ (કીબોર્ડ 1100 -> Enter = 0.8 mm થી 1.1 mm). 0.8 mm થી ઓછી પહોળાઈમાં સોય દોરો કાપી નાખે છે.', '<b>Short Stitches = 0.5 mm (શોર્ટ સ્ટીચ સિક્યુરિટી):</b> તીવ્ર વળાંક પર અંદરની બાજુ ટાંકા ગૂંચવાઈ ન જાય તે માટે ઓટોમેટિક શોર્ટ સ્ટીચ ફિલ્ટર.', '<b>Real Fabric Result (વાસ્તવિક કાપડ પરિણામ):</b> જમણી બાજુ રોયલ બ્લુ સિલ્ક ફેબ્રિક પર સોનેરી જરીના ઉપસેલા (3D Embossed) ચળકતા સાટિન સ્ટીચ ટાંકાનું ઉત્કૃષ્ટ પરિણામ.']
        ) + """

        <h3 style="color: var(--primary); margin: 20px 0 10px 0;">⚖️ F4 Column Symmetry vs F2 Simple Satin તુલના</h3>
        <table class="data-table">
            <thead><tr><th>પેરામીટર</th><th>F4 Column Symmetry (સિમેટ્રી પાઘડી)</th><th>F2 Simple Satin (અનસિમેટ્રી)</th></tr></thead>
            <tbody>
                <tr><td><b>આકાર સંતુલન</b></td><td>બંને બાજુ એકસરખો સપ્રમાણ વળાંક બને છે.</td><td>બંને બાજુ સાવ અલગ અલગ વળાંક અને આકાર હોઈ શકે.</td></tr>
                <tr><td><b>ક્લિકિંગ પદ્ધતિ</b></td><td>ડાબે એક ક્લિક, જમણે એક ક્લિક (જોડીમાં).</td><td>એક બાજુ આખી લાઇન દોરી Enter, પછી બીજી બાજુ.</td></tr>
                <tr><td><b>પહોળાઈ સેટિંગ</b></td><td>1100 લખી Enter આપવાથી સ્ટાન્ડર્ડ પહોળાઈ સેટ થાય છે.</td><td>હાથેથી બંને બાજુના અંતર દ્વારા પહોળાઈ નક્કી થાય છે.</td></tr>
                <tr><td><b>ખૂણા પોઇન્ટ્સ</b></td><td>'D' દબાવવાથી તીક્ષ્ણ ખૂણો (Square Point) પડે છે.</td><td>ખૂણા માટે અલગથી એંગલ લાઇન આપવી પડે છે.</td></tr>
                <tr><td><b>વળાંક પોઇન્ટ્સ</b></td><td>'O' દબાવવાથી સ્મૂથ ગોળાકાર (Curve Point) પડે છે.</td><td>વળાંક માટે નોડ્સને હેન્ડલ વડે એડજસ્ટ કરવા પડે છે.</td></tr>
                <tr><td><b>ન્યૂનતમ સ્પેસિંગ</b></td><td>ટાંકા વચ્ચેનું અંતર ઓછામાં ઓછું 0.8 mm હોવું જ જોઈએ.</td><td>ઓછામાં ઓછું 0.7 mm સ્પેસિંગ.</td></tr>
            </tbody>
        </table>

        <div class="callout callout-warning">
            <div class="callout-icon">⚠️</div>
            <div class="callout-content">
                <strong>પાઘડી બનાવતી વખતે સોય તૂટતી અટકાવવાનો ઉપાય:</strong>
                જ્યાં પાઘડીનો વળાંક એકદમ તીવ્ર (Sharp Turn) હોય ત્યાં અંદરની બાજુ ટાંકા ગૂંચવાઈ ન જાય તે માટે <b>Short Stitches = 0.5 mm</b> ઓન રાખો. જો અંદરની બાજુ ટાંકા ભેગા થશે તો દોરો વારંવાર કપાશે અને પ્રોડક્શન બગડશે.
            </div>
        </div>
    </div>
    """

    sec5 = """
    <div class="section-card" id="sec-punching">
        <div class="section-header">
            <div class="section-title">
                <span>⚡</span> Section 5: Step 4: Punching Mechanics & Essential Shortcuts
            </div>
            <span class="section-tag">પંચિંગ મિકેનિક્સ અને શોર્ટકટ્સ</span>
        </div>
        <p style="margin-bottom: 16px;">
            પંચિંગ એટલે માત્ર આકાર દોરવો નહીં, પણ મશીન કઈ સોયથી, કઈ દિશામાં અને કેટલા જમ્પ સાથે ચાલશે તેની તાર્કિક ગોઠવણી કરવી.
        </p>

        <div class="image-gallery">
            """ + img_card("13_Step4_Punching_Shortcuts_Mechanics.jpg", "Step 4: પંચિંગ મિકેનિક્સ શોર્ટકટ્સ", "Shift+X, Ctrl+D, Alt+Shift+V અને જમ્પ કંટ્રોલ નિયમો") + """
        </div>

        <table class="data-table">
            <thead><tr><th>શોર્ટકટ / નિયમ</th><th>પ્રેક્ટિકલ સમજૂતી અને પંચિંગ અસર</th></tr></thead>
            <tbody>
                <tr><td><span class="badge-code">Shift + X</span> (Start/End Swap)</td><td>ઓબ્જેક્ટનો શરૂઆતનો અને છેલ્લો પોઇન્ટ અરસપરસ બદલવા માટે. જો આગલો ઓબ્જેક્ટ ડાબે પતતો હોય તો આ કીથી નવા ઓબ્જેક્ટની શરૂઆત ડાબે લાવી શકાય છે.</td></tr>
                <tr><td><span class="badge-code">Ctrl + D</span> (Duplicate)</td><td>પસંદ કરેલા ઓબ્જેક્ટની તરત જ હૂબહૂ ડુપ્લિકેટ નકલ બનાવવા માટે.</td></tr>
                <tr><td><span class="badge-code">Alt + Shift + V</span> (Paste in Place)</td><td>સ્પેશિયલ પેસ્ટ કમાન્ડ - ઓબ્જેક્ટ સ્ક્રીન પર જે મૂળ જગ્યાએ હતો ત્યાં જ સચોટ એલાઇનમેન્ટ સાથે પેસ્ટ થાય છે.</td></tr>
                <tr><td><b>5 mm જમ્પ ગોલ્ડન રૂલ</b></td><td>જો બે ઓબ્જેક્ટ વચ્ચેનું અંતર 5 mm કરતાં વધારે હોય તો મશીનમાં જમ્પ ટ્રીમ આપવો અથવા વચ્ચે ટ્રાવેલ રન સ્ટીચ (Travel Stitch) ચલાવવી જેથી દોરો ખેંચાય નહીં.</td></tr>
                <tr><td><b>Pull Compensation (ખેંચાણ)</b></td><td>કાપડ જ્યારે ફ્રેમમાં તણાય ત્યારે ટાંકા અંદર ખેંચાઈ જાય છે. આથી હંમેશા 0.2 mm થી 0.35 mm પુલ કોમ્પેન્સેશન આપવું.</td></tr>
                <tr><td><b>Underlay (તળિયાના ટાંકા)</b></td><td>મુખ્ય સાટિન કે તતામી ચાલતા પહેલાં નીચે ઝીગઝેગ કે રન સ્ટીચનો પાયો હોવો જોઈએ જેથી કાપડમાં કરચલી ન પડે.</td></tr>
            </tbody>
        </table>
    </div>
    """

    sec6 = """
    <div class="section-card" id="sec-fkeys">
        <div class="section-header">
            <div class="section-title">
                <span>🎹</span> Section 6: Step 5: Function Keys Guide (F1 to F12)
            </div>
            <span class="section-tag">સ્ટીચ પ્રકારો અને F-કીઝ</span>
        </div>
        <p style="margin-bottom: 16px;">
            કીબોર્ડની F1 થી F12 કીઝ એ એમ્બ્રોઇડરી ડિઝાઇનિંગના હૃદય સમાન છે. તેનાથી સ્ટીચના પ્રકારો સીધા બદલાય છે.
        </p>

        <div class="image-gallery">
            """ + img_card("14_Step5_Function_Keys_F1_to_F9.jpg", "Step 5: F1 થી F9 ફંક્શન કીઝ", "Pro Stitch, Satin, Tatami, Column, Star, Parallel, Outline, Run, Triple Run") + """
            """ + img_card("15_Step5_F10_Motif_F11_F12_Cording.jpg", "Step 5: F10, F11 અને F12 કોર્ડિંગ", "F10 મોટીફ રન, F11 ડિઝાઇન ચેન્જ, F12 કોર્ડિંગ (Angle 50, 35, 21; Times 2)") + """
        </div>


        """ + comparison_card(
            "74_Compare_Cording_Dori_Vector_Drawing_vs_Real_Embroidery.jpg",
            "કોર્ડિંગ સરખામણી: F12 દોરી ઝિગઝેગ પંચિંગ vs વાસ્તવિક 3D દોરી વર્ક",
            "EmCAD F12 Cording Path vs Real Raised 3D Dori Embroidery",
            ['<b>Core Cord (મુખ્ય જાડી દોરી - પીળી સેન્ટ્રલ દોરી):</b> સોનેરી જરી કે સિલ્કની જાડી દોરી જે મશીનના ગાઇડ પાઇપમાંથી કાપડની સપાટી પર સતત પથરાય છે.', '<b>Needle Zigzag Tack Stitch (ઝિગઝેગ પકડ ટાંકો - લાલ ટાંકા):</b> સોય દોરીને કાપ્યા વગર તેની બંને બાજુ ડાબે-જમણે કૂદીને ઝિગઝેગ સ્ટીચ વડે કાપડ સાથે જકડે છે.', '<b>F12 Cording Parameter: Angle = 50, 35, 21; Times = 2:</b> વળાંક પર સોયનો એંગલ ૫૦°, ૩૫°, ૨૧° રહે છે અને દોરી બમણી મજબૂતાઈથી ટંકાય છે.', '<b>Lead-In Start Lock (શરૂઆતનો પેક ટાંકો):</b> દોરી શરૂ થતાં ૨ mm આગળથી દોરાનો રન સ્ટીચ ચલાવીને દોરીનો છેડો કાપડમાં દબાવવો.', '<b>Lead-Out End Lock (છેલ્લા છેડાનો ટાઇ-ઓફ):</b> દોરી પતે ત્યારે સોય ૩-૪ ટાંકા મારીને દોરો પેક કરે છે જેથી ધોવાયા પછી દોરીનો છેડો છૂટો ન પડે.', '<b>Island Cording (આઇલેન્ડ દોરી પદ્ધતિ):</b> મોટીફની અંદરનો ભાગ ખાલી રાખી માત્ર બહારની કિનારી પર જ જાડી દોરી ચલાવીને 3D આઉટલાઇન આપવી.', '<b>Real Fabric Result (વાસ્તવિક કાપડ પરિણામ):</b> જમણી બાજુ નેવી બ્લુ રોયલ વેલ્વેટ પર ઉપસેલી સોનેરી દોરીનું ઉત્કૃષ્ટ 3D એમ્બોસ્ડ હેવી લગ્ન-પોશાક વર્ક.']
        ) + """

        <table class="data-table">
            <thead><tr><th style="width: 60px;">કી</th><th style="width: 220px;">સ્ટીચ પ્રકાર (Stitch Type)</th><th>વિગતવાર સેટિંગ્સ અને ઉપયોગ</th></tr></thead>
            <tbody>
                <tr><td><span class="badge-code">F1</span></td><td><b>Pro Stitch Count / Seg / Beads</b></td><td>ડિઝાઇનના સ્ટીચ કાઉન્ટ અને સિક્વિન/બીડ્સ સેગમેન્ટ ઇન્ફોર્મેશન જોવા.</td></tr>
                <tr><td><span class="badge-code">F2</span></td><td><b>Simple Satin (અનસિમેટ્રી)</b></td><td>બંને બાજુ અલગ અલગ શેપ ધરાવતો સાદો સાટિન ટાંકો દોરવા.</td></tr>
                <tr><td><span class="badge-code">F3</span></td><td><b>Complex Fill / Tatami (તતામી)</b></td><td>મોટા એરિયા ભરવા માટે. તતામીની સ્ટાન્ડર્ડ ડેન્સિટી 0.45 mm અને સ્ટીચ લંબાઈ 4.0 mm.</td></tr>
                <tr><td><span class="badge-code">F4</span></td><td><b>Column Symmetry (પાગડી)</b></td><td>બંને બાજુ સરખો વળાંક ધરાવતી સ્ટાન્ડર્ડ પાઘડી દોરવા.</td></tr>
                <tr><td><span class="badge-code">F5</span></td><td><b>Star Stitch (તારલી)</b></td><td>ફૂલની વચ્ચે સુંદર તારલી કે સ્ટાર પેટર્ન બનાવવા.</td></tr>
                <tr><td><span class="badge-code">F6</span></td><td><b>Input Parallel</b></td><td>એકસરખી સમાંતર પહોળાઈ વાળી પટ્ટી દોરવા.</td></tr>
                <tr><td><span class="badge-code">F7</span></td><td><b>Outline Method</b></td><td>ઓબ્જેક્ટની ચોતરફ ઓટોમેટિક આઉટલાઇન રન સ્ટીચ મૂકવા.</td></tr>
                <tr><td><span class="badge-code">F8</span></td><td><b>Run Stitch (સિંગલ રન)</b></td><td>સિંગલ રનિંગ સ્ટીચ - સ્ટાન્ડર્ડ ટાંકા લંબાઈ 2.5 mm થી 3.0 mm.</td></tr>
                <tr><td><span class="badge-code">F9</span></td><td><b>Triple Run (Bean Stitch)</b></td><td>૩ વાર આગળ-પાછળ ચાલતી મજબૂત જાડી લાઇન (આઉટલાઇન હાઇલાઇટ માટે).</td></tr>
                <tr><td><span class="badge-code">F10</span></td><td><b>Motif Run</b></td><td>પસંદ કરેલી ડેકોરેટીવ મોટીફની ચેઇન લાઇન દોરવા.</td></tr>
                <tr><td><span class="badge-code">F11</span></td><td><b>By Stitch Type / Change</b></td><td>ચોક્કસ સ્ટીચ ટાઇપ સિલેક્ટ કરી આખી ડિઝાઇનમાં ફેરફાર કરવા.</td></tr>
                <tr><td><span class="badge-code">F12</span></td><td><b>Cording (દોરી વર્ક)</b></td><td>દોરી ટાંકવા માટે સ્પેશિયલ સેટિંગ: <b>Angle = 50, 35, 21; Times = 2</b>.</td></tr>
            </tbody>
        </table>

        <div class="callout callout-tip">
            <div class="callout-icon">💡</div>
            <div class="callout-content">
                <strong>F2 થી F3 કન્વર્ટ કરવાની સીક્રેટ ટ્રીક:</strong>
                જો તમે F2 (સાટિન) માં કોઈ મોટો શેપ દોરી લીધો હોય અને હવે તેને F3 (તતામી ફીલ) માં ફેરવવો હોય, તો ઓબ્જેક્ટ સિલેક્ટ કરી કીબોર્ડ પરથી <b>F3 દબાવો અને ૩ વખત Enter આપો!</b> ઓબ્જેક્ટ આપોઆપ પરફેક્ટ તતામી ફીલમાં કન્વર્ટ થઈ જશે.
            </div>
        </div>
    </div>
    """

    sec7 = """
    <div class="section-card" id="sec-repeats">
        <div class="section-header">
            <div class="section-title">
                <span>📐</span> Section 7: Step 6 & Step 12: Machine Repeats, Farma & Production Layout
            </div>
            <span class="section-tag">ફાર્મા અને રીપીટ સેટિંગ</span>
        </div>
        <p style="margin-bottom: 16px;">
            મોટા પાયે ઉત્પાદન (Production) માટે ફાર્મા સેટ કરવો અને રીપીટ બેસાડવા એ પંચરનું સૌથી જવાબદારીભર્યું કામ છે. 
            ફાર્મામાં ૧ mm ની ભૂલ મલ્ટી-હેડ મશીન પર હજારો મીટર કાપડ બગાડી શકે છે.
        </p>

        <div class="image-gallery">
            """ + img_card("16_Step6_Machine_Repeats_Lace_Sizes.jpg", "Step 6: મશીન રીપીટ અને લેસ સાઇઝ", "125, 250, 300, 330, 400, 500, 600, 700 mm રીપીટ") + """
            """ + img_card("39_Step12_Farma_400Width_390WorkingArea.jpg", "Step 12: ૪૦૦ mm ફ્રેમ -> ૩૯૦ mm એરિયા", "બંને બાજુ ૫ mm સેફ્ટી માર્જિન સાથે વાસ્તવિક પંચિંગ એરિયા") + """
            """ + img_card("40_Step12_Farma_Crossline_Center_X0_Y0.jpg", "Step 12: સેન્ટર ક્રોસલાઇન X=0, Y=0", "115 mm ગાઈડલાઇન ઓફસેટ સેટિંગ અને સેન્ટરિંગ") + """
            """ + img_card("41_Step12_Farma_Offset_Delete_Guidelines.jpg", "Step 12: ગાઈડલાઈન્સ ડીલીટ કરવી", "વધારાની ગાઈડલાઈન્સ હટાવી વર્કસ્પેસ ક્લીન કરવો") + """
            """ + img_card("42_Step12_Farma_Mirror_12point5_Percent_Steps.jpg", "Step 12: ૧૨.૫% સ્ટેપ રીપીટ ટેબલ", "૮ સ્ટેપ્સ: 12.5%, 25%, 37.5%, 50%, 62.5%, 75%, 87.5%, 100%") + """
            """ + img_card("43_Step12_Farma_16point5_Percent_Steps.jpg", "Step 12: ૧૬.૫% સ્ટેપ રીપીટ ટેબલ", "૬ સ્ટેપ્સ: 16.5%, 33%, 49.5%, 66%, 82.5%, 100%") + """
            """ + img_card("44_Step12_Box_Pattern_300_150_Offset.jpg", "Step 12: બોક્સ પેટર્ન ૩૦૦ mm / ૧૫૦ mm", "હાફ-ડ્રોપ બ્રિક પેટર્ન અને બ્રેક 'B' કમાન્ડ") + """
            """ + img_card("45_Step12_Box_Pattern_Coloring_And_Border.jpg", "Step 12: બોક્સ પેટર્ન કલરિંગ & બોર્ડર", "કલર સિક્વન્સિંગ અને કનેક્ટર લાઇન સેટિંગ") + """
            """ + img_card("46_Step12_Net_Embroidery_Calculations.jpg", "Step 12: નેટ સાડી ગણતરી", "૪૩ ઇંચ + ૫ ઇંચ બોર્ડર = ૪૮ ઇંચ (૧૨૦૦ mm હાઇટ)") + """
            """ + img_card("47_Step12_Scanner_Setup_Canon_MF_Toolbox.jpg", "Step 12: સ્કેનર સેટઅપ Canon MF", "Custom 1, 300 થી 600 DPI રિઝોલ્યુશન") + """
            """ + img_card("48_Step12_Farma_Title_Page.jpg", "Step 12: ફાર્મા માસ્ટર ગાઇડ ટાઇટલ", "ઓરિજિનલ વર્કશોપ ફાર્મા સેટઅપ સમરી") + """
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 20px; margin: 20px 0;">
            <div>
                <h3 style="color: var(--primary); margin-bottom: 8px;">🔢 ૧૨.૫% સ્ટેપ રીપીટ ટેબલ (૮ સ્ટેપ્સ)</h3>
                <table class="data-table">
                    <thead><tr><th>પગથિયું</th><th>ટકાવારી ગણતરી</th><th>કુલ ટકાવારી</th></tr></thead>
                    <tbody>
                        <tr><td>સ્ટેપ ૧</td><td>12.5%</td><td><b>12.5%</b></td></tr>
                        <tr><td>સ્ટેપ ૨</td><td>12.5% + 12.5%</td><td><b>25.0%</b></td></tr>
                        <tr><td>સ્ટેપ ૩</td><td>25.0% + 12.5%</td><td><b>37.5%</b></td></tr>
                        <tr><td>સ્ટેપ ૪</td><td>37.5% + 12.5%</td><td><b>50.0%</b></td></tr>
                        <tr><td>સ્ટેપ ૫</td><td>50.0% + 12.5%</td><td><b>62.5%</b></td></tr>
                        <tr><td>સ્ટેપ ૬</td><td>62.5% + 12.5%</td><td><b>75.0%</b></td></tr>
                        <tr><td>સ્ટેપ ૭</td><td>75.0% + 12.5%</td><td><b>87.5%</b></td></tr>
                        <tr><td>સ્ટેપ ૮</td><td>87.5% + 12.5%</td><td><b>100.0%</b></td></tr>
                    </tbody>
                </table>
            </div>

            <div>
                <h3 style="color: var(--primary); margin-bottom: 8px;">🔢 ૧૬.૫% સ્ટેપ રીપીટ ટેબલ (૬ સ્ટેપ્સ)</h3>
                <table class="data-table">
                    <thead><tr><th>પગથિયું</th><th>ટકાવારી ગણતરી</th><th>કુલ ટકાવારી</th></tr></thead>
                    <tbody>
                        <tr><td>સ્ટેપ ૧</td><td>16.5%</td><td><b>16.5%</b></td></tr>
                        <tr><td>સ્ટેપ ૨</td><td>16.5% + 16.5%</td><td><b>33.0%</b></td></tr>
                        <tr><td>સ્ટેપ ૩</td><td>33.0% + 16.5%</td><td><b>49.5%</b></td></tr>
                        <tr><td>સ્ટેપ ૪</td><td>49.5% + 16.5%</td><td><b>66.0%</b></td></tr>
                        <tr><td>સ્ટેપ ૫</td><td>66.0% + 16.5%</td><td><b>82.5%</b></td></tr>
                        <tr><td>સ્ટેપ ૬</td><td>82.5% + 16.5%</td><td><b>~ 100.0%</b></td></tr>
                    </tbody>
                </table>
            </div>
        </div>

        <div class="callout callout-tip">
            <div class="callout-icon">💡</div>
            <div class="callout-content">
                <strong>૪૦૦ mm ફાર્માનો નિયમ:</strong>
                મશીન ફ્રેમની પહોળાઈ 400 mm હોય તો વાસ્તવિક પંચિંગ એરિયા 390 mm જ રાખવો. સેન્ટરમાં ક્રોસલાઇન (X=0, Y=0) દોરી બંને બાજુ 195 mm નું માર્જિન મળે છે.
            </div>
        </div>
    </div>
    """

    sec8 = """
    <div class="section-card" id="sec-motif">
        <div class="section-header">
            <div class="section-title">
                <span>🌺</span> Section 8: Step 7: Custom Motif Creation & Motif Fill
            </div>
            <span class="section-tag">મોટીફ નિર્માણ અને ફીલ</span>
        </div>
        <p style="margin-bottom: 16px;">
            કસ્ટમ મોટીફ એટલે આપણી પોતાની બનાવેલી નાની ડિઝાઇન (દા.ત. પાંદડી, સ્ટાર કે કેરી) જેને ચેઇન તરીકે કે આખા એરિયામાં બેકગ્રાઉન્ડ ફીલ તરીકે વાપરી શકાય છે.
        </p>

        <div class="image-gallery">
            """ + img_card("17_Step7_Motif_Creation_And_Motif_Fill.jpg", "Step 7: કસ્ટમ મોટીફ નિર્માણ", "Other -> Make Motif મેનુ, Start/End અલાઇનમેન્ટ અને F10 / F3 નો ઉપયોગ") + """
        </div>

        <table class="data-table">
            <thead><tr><th style="width: 140px;">સ્ટેપ ક્રમ</th><th>પ્રેક્ટિકલ પ્રક્રિયા અને પંચિંગ નિયમ</th></tr></thead>
            <tbody>
                <tr><td><b>પગથિયું ૧: ઓબ્જેક્ટ ડ્રોઇંગ</b></td><td>સ્ક્રીન પર એક નાનો, સુંદર શેપ દોરો (દા.ત. 5 mm x 5 mm ની નાની કેરી કે પાંદડી).</td></tr>
                <tr><td><b>પગથિયું ૨: Start/End Alignment</b></td><td>ઓબ્જેક્ટનો Start Point (શરૂઆત) અને End Point (અંત) બરાબર એક જ આડી લાઇન પર સેટ કરો. આ સૌથી મહત્વનું છે.</td></tr>
                <tr><td><b>પગથિયું ૩: Make Motif મેનુ</b></td><td>ઓબ્જેક્ટ સિલેક્ટ કરો -> મેનુ બારમાં <b>Other -> Make Motif</b> પર ક્લિક કરો.</td></tr>
                <tr><td><b>પગથિયું ૪: રેફરન્સ પોઇન્ટ્સ</b></td><td>ઓબ્જેક્ટની ડાબી બાજુ ક્લિક કરો (Start) અને જમણી બાજુ ક્લિક કરો (End). નવી મોટીફનું નામ આપી Save કરો.</td></tr>
                <tr><td><b>પગથિયું ૫: F10 Motif Run</b></td><td>હવે કીબોર્ડ પરથી <b>F10</b> દબાવી લાઇન દોરશો એટલે આ નવી મોટીફ લાઇન પર દોડાશે.</td></tr>
                <tr><td><b>પગથિયું ૬: F3 Motif Fill</b></td><td>કોઈપણ મોટા સર્કલ કે શેપમાં તતામીને બદલે મોટીફ ભરવા Property માં જઈ Motif Fill સિલેક્ટ કરો.</td></tr>
            </tbody>
        </table>
    </div>
    """

    sec9 = """
    <div class="section-card" id="sec-density">
        <div class="section-header">
            <div class="section-title">
                <span>✨</span> Section 9: Step 8: Advanced Stitch Effects & Density Control
            </div>
            <span class="section-tag">સ્પેશિયલ ઇફેક્ટ્સ અને ડેન્સિટી</span>
        </div>
        <p style="margin-bottom: 16px;">
            ટાંકાની ઘનતા (Density) અને પેટર્ન સ્પ્લિટ ડિઝાઇનને રીચ અને પ્રીમિયમ લુક આપે છે. ખોટી ડેન્સિટીથી કાપડ ફાટી જાય છે અથવા સફેદ કાપડ દેખાય છે.
        </p>

        <div class="image-gallery">
            """ + img_card("18_Step8_Satin_Density_And_Tatami_Split.jpg", "Step 8: સાટિન ડેન્સિટી & તતામી સ્પ્લિટ", "સાટિન ડેન્સિટી 0.4 થી 0.8 mm અને તતામી #20 ડિઝાઇનર પેટર્ન") + """
            """ + img_card("19_Step8_Zigzag_EStitch_PatternSplit_Contour.jpg", "Step 8: ઝિગઝેગ, E-Stitch & કોન્ટૂર", "ઝિગઝેગ સ્ટીચ, એપ્લિક કાંગરી E-Stitch અને કોન્ટૂર શોર્ટિંગ") + """
        </div>

        <table class="data-table">
            <thead><tr><th>કાપડ પ્રકાર / ઇફેક્ટ</th><th>સ્ટાન્ડર્ડ સેટિંગ</th><th>પ્રેક્ટિકલ ઉપયોગ અને પરિણામ</th></tr></thead>
            <tbody>
                <tr><td><b>હેવી સિલ્ક / પોલિએસ્ટર</b></td><td><b>0.40 mm થી 0.45 mm</b></td><td>ટાંકા એકદમ ભરેલા અને ચળકાટવાળા દેખાશે.</td></tr>
                <tr><td><b>મીડીયમ જ્યોર્જેટ / કોટન</b></td><td><b>0.45 mm થી 0.50 mm</b></td><td>સ્ટાન્ડર્ડ પ્રોડક્શન ડેન્સિટી.</td></tr>
                <tr><td><b>લાઈટ નેટ / શિફોન</b></td><td><b>0.60 mm થી 0.80 mm</b></td><td>કાપડ પાતળું હોવાથી ટાંકા હળવા રાખવા જેથી કાપડ ખેંચાઈ ન જાય.</td></tr>
                <tr><td><b>Forward / Backward Ratio</b></td><td>Forward: 1 -> 3 | Backward: 1.5 -> 5</td><td>ટાંકા આગળ વધવાનો અને પાછા વળવાનો ગુણોત્તર.</td></tr>
                <tr><td><b>Tatami Pattern Split (#20)</b></td><td>20 અલગ અલગ ડિઝાઇનર પેટર્ન</td><td>તતામીમાં સાદા ટાંકાને બદલે વેવ, ડાયમંડ કે ચેકર પેટર્ન પડે છે.</td></tr>
                <tr><td><b>E-Stitch (કાંગરી)</b></td><td>એક બાજુ રન અને બીજી બાજુ કાંટા</td><td>એપ્લિકના છેડા લોક કરવા અને બોર્ડર પર કાંગરી બનાવવા.</td></tr>
            </tbody>
        </table>
    </div>
    """

    sec10 = """
    <div class="section-card" id="sec-shading">
        <div class="section-header">
            <div class="section-title">
                <span>🎨</span> Section 10: Step 9: 9-Needle Photo Setup, Color Shading & Florentine Effects
            </div>
            <span class="section-tag">શેડિંગ અને ફ્લોરેન્ટાઇન</span>
        </div>
        <p style="margin-bottom: 16px;">
            આ સેક્શનમાં ૯-સોય વાળા મશીન પર ફોટો સેટ કરવો, ગ્રેડિયન્ટ શેડિંગ આપવું, ફ્લોરેન્ટાઇન વળાંક અને આઇલેન્ડ કોર્ડિંગની વિગતવાર સમજૂતી છે.
        </p>

        <div class="image-gallery">
            """ + img_card("20_Step9_9Needle_Photo_Setup_Sequencing.jpg", "Step 9: ૯-સોય ફોટો સેટઅપ", "૨૦૦ mm એરિયા, ક્રોસલાઇન X=0, Y=0, +-100mm ગાઈડલાઇન્સ અને 1 થી 6 કીઝ") + """
            """ + img_card("21_Step9_Shading_Flower_Vector_Circle.jpg", "Step 9: શેડિંગ ફ્લાવર સર્કલ", "વેક્ટર સર્કલ ટ્રેસિંગ અને મલ્ટી-કલર ગ્રેડિયન્ટ પેટર્ન") + """
            """ + img_card("22_Step9_Perpendicular_Fill_Cross_Point.jpg", "Step 9: ૯૦° પરપેન્ડીક્યુલર તતામી ફીલ", "કાટખૂણે છેદતા ટાંકા અને ક્રોસ પોઇન્ટ અલાઇનમેન્ટ") + """
            """ + img_card("23_Step9_Florentine_Effect_Curved_Fill.jpg", "Step 9: ફ્લોરેન્ટાઇન ઇફેક્ટ", "વળાંકવાળી એંગલ લાઇન્સ સાથે મોજા જેવો 3D લુક") + """
            """ + img_card("24_Step9_Cording_Neck_Island_Coil.jpg", "Step 9: કોર્ડિંગ નેકલાઇન & આઇલેન્ડ કોઈલ", "કોર્ડિંગ નેકલાઇન, આઇલેન્ડ સ્ટીચ અને કોઈલ વળાંક સેટિંગ") + """
            """ + img_card("25_Step9_Island_Cord_Outline_Method.jpg", "Step 9: આઇલેન્ડ કોર્ડ આઉટલાઇન પદ્ધતિ", "વચલો ભાગ ખાલી રાખી ચોતરફ દોરી ટાંકવાની રીત") + """
        </div>


        """ + comparison_card(
            "73_Compare_Shading_Flower_Vector_Drawing_vs_Real_Embroidery.jpg",
            "શેડિંગ સરખામણી: ૯૦° પરપેન્ડીક્યુલર તતામી vs વાસ્તવિક ગ્રેડિયન્ટ ફૂલ",
            "EmCAD Vector Contours vs Real Multi-Needle Embroidered Flower Petal",
            ['<b>Needle 1: Dark Red Base Layer (તળિયું):</b> પાંખડીના નીચેના ભાગમાં ઘાટો લાલ રંગ જે ફૂલની ઊંડાઈ અને પડછાયો (Shadow) દર્શાવે છે.', '<b>Needle 2: Pink Mid-Tone Layer (વચ્ચેનો ભાગ):</b> મધ્યમાં ગુલાબી રંગ જે નીચેના ઘાટા લાલ સાથે ૨ થી ૩ mm અંદરોઅંદર ભળી જાય છે.', '<b>Needle 3: Ivory / White Tip (ઉપરની કિનારી):</b> પાંખડીની ટોચ પર આછો સફેદ/ક્રીમ રંગ જે પ્રકાશનો ચમકારો (Highlight) ઊભો કરે છે.', '<b>Perpendicular 90° Tatami Fill (કાટખૂણે છેદતી તતામી):</b> સામાન્ય તતામી કરતાં ૯૦ ડિગ્રી કાટખૂણે ટાંકા છેદે છે જેથી સૂર્યપ્રકાશમાં ડબલ-શેડ ચમક પેદા થાય છે.', '<b>Florentine Effect (મોજા જેવો વળાંક):</b> પાંખડીમાં સીધી લીટીને બદલે વળાંકવાળી એંગલ લાઇન વડે પાણીના મોજા જેવો લુક (Curved Angle Fill).', '<b>Color Sequence Keys (Keys 1 to 9):</b> કીબોર્ડ 1 થી 9 કી વડે ૯-સોય મશીનના દોરાના કલર સ્ટેપ-બાય-સ્ટેપ બદલવામાં આવે છે.', '<b>Real Fabric Result (વાસ્તવિક કાપડ પરિણામ):</b> જમણી બાજુ ક્રીમ સિલ્ક કાપડ પર ઘાટા લાલથી ગુલાબી અને સફેદ રંગમાં વણાયેલી કળાત્મક પાંખડીઓનું કુદરતી કલર-શેડિંગ.']
        ) + """

        <div class="callout callout-tip">
            <div class="callout-icon">💡</div>
            <div class="callout-content">
                <strong>ફ્લોરેન્ટાઇન અને પરપેન્ડીક્યુલર ફીલનો જાદુ:</strong>
                ૧. <b>Perpendicular Fill:</b> સામાન્ય તતામી એક જ દિશામાં ચાલે છે, જ્યારે 90° પરપેન્ડીક્યુલર ફીલમાં ટાંકા એકબીજાને કાટખૂણે છેદે છે, જેથી સૂર્યપ્રકાશમાં કાપડ પર અદભુત ડબલ-શેડ ચમક આવે છે.<br/>
                ૨. <b>Florentine Effect:</b> પાંદડી કે પાંખડીમાં સીધી એંગલ લાઇન આપવાને બદલે વળાંકવાળી (Curved) એંગલ લાઇન આપવાથી ટાંકા પાણીના મોજાની જેમ વળે છે અને કુદરતી 3D લુક મળે છે.<br/>
                ૩. <b>Island Cord:</b> વચ્ચેનો આખો ભાગ ખાલી રાખી માત્ર કિનારી પર જ જાડી દોરી ટાંકવા માટે F12 અને આઉટલાઇન ટૂલનો સંયુક્ત ઉપયોગ કરવો.
            </div>
        </div>
    </div>
    """

    sec11 = """
    <div class="section-card" id="sec-transform">
        <div class="section-header">
            <div class="section-title">
                <span>🔄</span> Section 11: Step 10: Transform, Seg 3mm & Motif Lace
            </div>
            <span class="section-tag">ટ્રાન્સફોર્મ અને લેસ સેટિંગ</span>
        </div>
        <p style="margin-bottom: 16px;">
            લેસ બોર્ડર અને પટ્ટી બનાવતી વખતે ટ્રાન્સફોર્મ ટૂલ અને ચોક્કસ સેગમેન્ટ અંતર (Seg 3 mm) ખૂબ ઉપયોગી બને છે.
        </p>

        <div class="image-gallery">
            """ + img_card("26_Step10_Transform_Seg_Motif_Lace.jpg", "Step 10: ટ્રાન્સફોર્મ સ્ટીચ & લેસ", "સાટિનથી રન કન્વર્ટ, સેગમેન્ટ ૩ mm ગાળો અને મોટીફ લેસ બોર્ડર") + """
        </div>

        <table class="data-table">
            <thead><tr><th style="width: 220px;">ફીચર</th><th>પંચિંગ પદ્ધતિ અને મહત્વ</th></tr></thead>
            <tbody>
                <tr><td><b>Transform Satin to Run</b></td><td>ઓબ્જેક્ટ પ્રોપર્ટીમાં જઈ સાટિનને સીધું રન સ્ટીચમાં બદલી શકાય છે.</td></tr>
                <tr><td><b>Seg 3.0 mm Spacing</b></td><td>લેસના કાંગરા કે બોર્ડરમાં બે મોટીફ વચ્ચે બરાબર 3 mm નો નિયમિત ગાળો રાખવો.</td></tr>
                <tr><td><b>Motif Lace Border</b></td><td>સાડીની કિનારી માટે મોટીફ ચેઇન બનાવી તેની બંને બાજુ સપોર્ટ રન સ્ટીચ ચલાવવી.</td></tr>
            </tbody>
        </table>
    </div>
    """

    sec12 = """
    <div class="section-card" id="sec-sequin-beads">
        <div class="section-header">
            <div class="section-title">
                <span>📿</span> Section 12: Sequin & Beads Technology (Step 11 & Step 16)
            </div>
            <span class="section-tag">સિક્વિન અને બીડ્સ સંપૂર્ણ ગાઇડ</span>
        </div>
        <p style="margin-bottom: 16px;">
            આજના સુરત માર્કેટમાં <b>સિક્વિન (ટિકી) અને બીડ્સ (મોતી / કટદાણા)</b> નું કામ સૌથી વધુ નફો આપે છે. 
            દહાઓ મશીનમાં સિક્વિન ડિવાઇસ અને બીડ્સ ડિવાઇસને ચોક્કસ પંચિંગ પેરામીટર્સ જોઈએ છે.
        </p>

        <h3 style="color: var(--primary); margin: 20px 0 10px 0;">🎛️ Sequin & Beads Object Property Dialogs</h3>
        <div class="image-gallery">
            """ + img_card("27_Dialog_ObjectProperty_ExpandToFit.jpg", "Expand To Fit", "સિક્વિન આઉટલાઇનથી બહાર સુધી ફેલાય છે") + """
            """ + img_card("28_Dialog_ObjectProperty_ContractToFit.jpg", "Contract To Fit", "સિક્વિન અંદર સંકોચાઈને ચોખ્ખો માર્જિન રાખે છે") + """
            """ + img_card("29_Dialog_ObjectProperty_Position_Edge_Fit.jpg", "Position Edge Fit", "કિનારી પર સિક્વિનનું સચોટ ડ્રોપ સેટિંગ") + """
            """ + img_card("30_Dialog_ObjectProperty_Position_Detail.jpg", "Position Detail", "ઓફસેટ, સ્પેસિંગ અને એંગલ પેરામીટર્સ") + """
            """ + img_card("31_Step11_Beads_Config_General.jpg", "Beads General Config", "બીડ્સ ડિવાઇસ એક્ટિવેશન અને સ્ટીચ મોડ") + """
            """ + img_card("32_Step11_Beads_Size_Height_Spray.jpg", "Beads Size & Height", "બીડ્સ સાઇઝ, ઊંચાઈ અને સ્પ્રે ઇફેક્ટ") + """
            """ + img_card("33_Step11_Beads_Types_A_B_C_D_Sizes.jpg", "Beads Types A, B, C, D", "બીડ્સ ટાઇપ્સ અને તેમના ચોક્કસ માપ") + """
            """ + img_card("34_Step11_Single_Bead_AltCapsLock_Angle.jpg", "Single Bead & Alt+CapsLock", "સિંગલ બીડ એડજસ્ટમેન્ટ અને ૯ ડિગ્રી રોટેશન") + """
            """ + img_card("35_Dialog_ObjectProperty_OverlapSew.jpg", "Overlap Sew", "સિક્વિન એકબીજા પર ચડાવી માછલીની છાલ જેવો લુક") + """
            """ + img_card("36_Dialog_ObjectProperty_Straight_StitchLength.jpg", "Straight Stitch Length", "ટાંકાની સીધી લંબાઈ સેટિંગ") + """
            """ + img_card("37_Dialog_ObjectProperty_Position_Fit_Underlay.jpg", "Position Fit & Underlay", "બીડ્સ નીચે અંડરલે બેઝ સ્ટીચ સેટિંગ") + """
            """ + img_card("38_Dialog_MarginProcess_Minimize_Margin.jpg", "Minimize Margin", "કિનારી પરથી બહાર નીકળતી ટિકી અટકાવવી") + """
            """ + img_card("62_Step16_Beads_Sizes_Heights_Taka_Table.jpg", "Step 16: બીડ્સ ટાંકા (Taka) ટેબલ", "બીડ્સ સાઇઝ મુજબ મશીન ટાંકા લંબાઈનું માસ્ટર ટેબલ") + """
            """ + img_card("63_Step16_Text_Tool_Beds_Seq_Pattern_45Deg.jpg", "Step 16: ટેક્સ્ટ ટૂલ & ૪૫° પેટર્ન", "બીડ્સ ટેક્સ્ટ અને ૪૫ ડિગ્રી એંગલ લાઇન") + """
            """ + img_card("64_Step16_Beads_Breakdown_AltY_AltB_Split.jpg", "Step 16: બીડ્સ બ્રેકડાઉન", "Arrange -> Break Down, Alt+Y કટ અને Alt+B સ્પ્લિટ") + """
            """ + img_card("65_Step16_Fix_Adjust_CtrlA_Offset_Fit.jpg", "Step 16: ફિક્સ એડજસ્ટ", "Ctrl+A -> Stitch -> Fix Adjust થી સોયના કાણાં રીપેર") + """
        </div>


        """ + comparison_card(
            "70_Compare_Sequin_Vector_Drawing_vs_Real_Embroidery.jpg",
            "સિક્વિન સરખામણી: Fix Type 26 ત્રિકોણ લોક vs વાસ્તવિક ઓવરલેપિંગ ટિકી",
            "EmCAD Sequin Drop Path vs Real Metallic Sequins on Fabric",
            ['<b>Sequin Metallic Disc (ટિકી સર્કલ):</b> સોનેરી કે સિલ્વર મેટાલિક ચમકતી પતરી, સામાન્ય વ્યાસ 2.0 mm, 3.0 mm અથવા 5.0 mm.', '<b>Center Needle Hole (મધ્ય સોયનું કાણું):</b> ટિકીના કેન્દ્રમાં આવેલું કાણું, જ્યાં સોય નીચે ઊતરીને ટિકીને દોરા વડે કાપડ સાથે જકડી રાખે છે.', '<b>Overlap Sew (માછલીની છાલ જેવો ઓવરલેપ લુક):</b> સિક્વિન ૪૦% થી ૫૦% એકબીજા પર ચડીને બેસે છે જેથી વચ્ચેનું બેઝ કાપડ બિલકુલ દેખાતું નથી.', '<b>Fix Type 26 (3-Point Triangle Lock / તીરછા-ત્રિકોણ લોક ટાંકો):</b> કાણામાંથી ૩ તરફ ૧૨૦° ના ખૂણે દોરાના ટાંકા મારીને ત્રિકોણ આકારે પેક કરવામાં આવે છે જેથી ધોવાયા પછી પણ ટિકી ઊખડે નહીં.', '<b>Drop Sequin Dir (ટિકી પડવાની દિશા):</b> મશીન હેડ કઈ દિશામાં આગળ વધી રહ્યું છે (Any, 0°, 90°) તે મુજબ ટિકી આપોઆપ એકબીજાની પાછળ ડ્રોપ થાય છે.', '<b>Expand to Fit vs Contract to Fit:</b> ડિઝાઇનની આઉટલાઇનથી ટિકી બહાર સુધી ફેલાવવી (Expand) કે અંદર સંકોચાઈને સેફ માર્જિન રાખવું (Contract).', '<b>Tie Stitch (લોક સ્ટીચ):</b> સિક્વિન પટ્ટી શરૂ થતાં અને પૂરી થતાં ૩-૪ નાના ટાંકા મારીને દોરો ગાંઠવામાં આવે છે.', '<b>Real Fabric Result (વાસ્તવિક કાપડ પરિણામ):</b> જમણી બાજુ એમેરાલ્ડ ગ્રીન જ્યોર્જેટ કાપડ પર ગોલ્ડ અને સિલ્વર મેટાલિક ટિકીનું આબેહૂબ માછલીની છાલ જેવું હાઈ-ફિનિશિંગ એમ્બ્રોઇડરી.']
        ) + """

        """ + comparison_card(
            "71_Compare_Beads_Vector_Drawing_vs_Real_Embroidery.jpg",
            "બીડ્સ સરખામણી: મોતી અને કટદાણા ટાંકા vs વાસ્તવિક લક્ઝરી બીડ્સ વર્ક",
            "EmCAD Beads Spacing & Taka Table vs Real Glass Pearls & Bugle Beads",
            ['<b>Round Pearl Beads (Beads A - ગોળ મોતી):</b> સફેદ/ક્રીમ ગોળ મોતી (1.7 mm, 2.0 mm, 2.5 mm). સ્ટાન્ડર્ડ મશીન ટાંકો = 2.15 mm થી 2.30 mm.', '<b>Cutdana Bugle Pipe (Beads B - કાચની નળી / કટદાણા):</b> 4.0 mm લાંબી હેક્સાગોનલ કાચની નળી. મશીન ટાંકો લંબાઈ = 4.50 mm (નળી કરતાં 0.5 mm વધુ).', '<b>Taka Distance (ટાંકાનું ચોક્કસ અંતર):</b> સોયના બે પંચ વચ્ચેનું અંતર. જો ટાંકો નળી કરતાં નાનો હશે તો સોય કાચ સાથે અથડાઈને તૂટી જશે અને મશીન બંધ પડશે.', '<b>Alt + CapsLock (૯° એંગલ રોટેશન):</b> કટદાણાની નળીને ડિઝાઇનની દિશા મુજબ ૯ ડિગ્રીના સ્ટેપમાં ત્રાંસી ફેરવીને બેસાડવાની શોર્ટકટ કી.', '<b>Break Down (Alt+Y Cut / Alt+B Split):</b> ખૂણા પર બીડ્સ લાઇનને અલગ કરી સોય ફ્રી કરવા માટે Arrange -> Break Down કમાન્ડ.', '<b>Fix Adjust (Ctrl + A -> Fix Adjust):</b> પંચિંગ પૂર્ણ થયા પછી ઓવરલેપિંગ કાણાં અને ડબલ બીડ્સ ફિલ્ટર કરી કાઢી નાખવાનું ટૂલ.', '<b>Short Stitches = 0.5 mm સિક્યુરિટી:</b> ટર્નિંગ પોઇન્ટ પર સોય કાચની નળીને અડ્યા વગર સલામત રીતે બહાર નીકળી જાય તે માટે.', '<b>Real Fabric Result (વાસ્તવિક કાપડ પરિણામ):</b> જમણી બાજુ મરૂન રોયલ વેલ્વેટ ફેબ્રિક પર હાથવણાટ જેવી ઉત્કૃષ્ટ ફિનિશિંગ સાથે ગોલ્ડન કટદાણા અને શુદ્ધ સફેદ મોતીનું કળાત્મક સંયોજન.']
        ) + """

        <h3 style="color: var(--primary); margin: 25px 0 10px 0;">📊 Beads Size, Height & Machine Taka (ટાંકો) સ્ટાન્ડર્ડ ટેબલ</h3>
        <table class="data-table">
            <thead>
                <tr>
                    <th>બીડ્સ પ્રકાર</th>
                    <th>વાસ્તવિક સાઇઝ</th>
                    <th>ઊંચાઈ (Height)</th>
                    <th>મશીન ટાંકો (Taka)</th>
                    <th>ઉપયોગ અને મશીન પ્રકાર</th>
                </tr>
            </thead>
            <tbody>
                <tr><td><b>Beads A (1.7 mm)</b></td><td>2.00 mm</td><td>1.55 mm</td><td><b>2.15 mm</b></td><td>ઝીણા મોતી (Micro Pearls) માટે.</td></tr>
                <tr><td><b>Beads A (2.0 mm)</b></td><td>2.25 mm</td><td>1.75 mm</td><td><b>2.30 mm</b></td><td>સ્ટાન્ડર્ડ મોતી (સૌથી વધુ વપરાશ).</td></tr>
                <tr><td><b>Beads A (2.5 mm)</b></td><td>2.50 mm</td><td>1.75 mm</td><td><b>2.40 mm</b></td><td>મોટા મોતી.</td></tr>
                <tr><td><b>Beads B (3.0 mm)</b></td><td>3.00 mm</td><td>2.45 mm</td><td><b>2.40 mm</b></td><td>રાઉન્ડ બીડ્સ (ગોળ મણકા).</td></tr>
                <tr><td><b>Beads B (4.0 mm Pipe)</b></td><td>2.40 mm</td><td>3.80 mm</td><td><b>4.50 mm</b></td><td>લાંબી કાચની નળી (કટદાણા / Bugle Beads).</td></tr>
                <tr><td><b>Beads C / D (5 - 6 mm)</b></td><td>2.00 mm</td><td>6.00 mm</td><td><b>6.00 mm</b></td><td>જમ્બો પાઇપ અને સ્પેશિયલ હેવી બીડ્સ.</td></tr>
            </tbody>
        </table>

        <h3 style="color: var(--primary); margin: 28px 0 12px 0;">🌟 હાઇ-એન્ડ સિક્વિન & બીડ્સ ટેકનોલોજી: ડબલ સ્ટેકિંગ અને કર્વ્ડ એલાઇનમેન્ટ</h3>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(340px, 1fr)); gap: 16px; margin-bottom: 20px;">
            <div class="anim-card">
                <div class="anim-card-header">
                    <h4><span>🌟</span> ડબલ સિક્વિન સ્ટેકિંગ (5mm + 3mm)</h4>
                    <span class="badge-code">Concentric Star Lock</span>
                </div>
                <div class="anim-container">
                    <img src="emCad_organized_assets/anim_sequin_double_stack.gif" alt="Sequin Double Stack" loading="lazy">
                </div>
                <div class="anim-caption">
                    <b>ટેકનિક:</b> Device A (5mm Base) + Device B (3mm Top) એકબીજા પર કેન્દ્રિત થઈ સિંગલ સ્ટ્રાઇકથી લોક થાય છે.
                </div>
            </div>

            <div class="anim-card">
                <div class="anim-card-header">
                    <h4><span>🌿</span> વળાંકવાળા પાથ પર બીડ્સ ૯° ટિલ્ટ</h4>
                    <span class="badge-code">Alt + CapsLock 9°</span>
                </div>
                <div class="anim-container">
                    <img src="emCad_organized_assets/anim_beads_curved_contour.gif" alt="Beads Curved Contour" loading="lazy">
                </div>
                <div class="anim-caption">
                    <b>ટેકનિક:</b> એસ-કર્વ વળાંક પર સોયની દિશા સ્પર્શક (Tangent) મુજબ ૯° ના સ્ટેપમાં ગોઠવાય છે જેથી કાચની નળી તૂટતી નથી.
                </div>
            </div>
        </div>

        """ + comparison_card(
            "76_Compare_Stacked_Sequin_Beads_Vector_vs_Real.jpg",
            "સ્ટેક્ડ સિક્વિન & બીડ્સ સરખામણી: ડ્યુઅલ ડ્રોપ vs રીયલ કુતૂર ફેબ્રિક",
            "EmCAD Dual Sequin Drop + Bugle Bead Radiation vs Real Bridal Haute-Couture",
            ['<b>Dual Sequin Drop (Device A 5mm + Device B 3mm):</b> નીચે ૫mm મોટી ગોલ્ડન બેઝ ટિકી અને ઉપર ૩mm નાની સિલ્વર હોલોગ્રાફિક ટિકી.', '<b>Concentric Center Lock:</b> બંને ટિકીના સેન્ટર કાણામાંથી ૧ જ સોય ઊતરીને ૪-પોઇન્ટ સ્ટાર લૉક મારે છે.', '<b>Cutdana Radial Array (૪.૫૦ mm ટાંકો):</b> ફૂલની આસપાસ સૂર્યના કિરણોની જેમ ગોઠવાયેલી કાચની નળીઓ, ટાંકો ૪.૫૦ mm રાખવો.', '<b>Alt + CapsLock ૯° ટેન્જન્ટ એંગલ:</b> ગોળાકારમાં ફરતી વખતે કટદાણાની નળીઓ સોય સામે સીધી ૯૦° એંગલે ગોઠવાય છે જેથી કાચ તૂટતો નથી.', '<b>Pearl Halo Ring (૨.૩૦ mm મોતી):</b> વચ્ચે ૬mm મોતી અને ફરતે ૨mm નાના મોતીની રીંગ.', '<b>Real Fabric Result (વાસ્તવિક કાપડ પરિણામ):</b> જમણી બાજુ મરૂન સિલ્ક નેટ ફેબ્રિક પર લક્ઝરી ઇન્ડિયન બ્રાઇડલ હેવી એમ્બ્રોઇડરી, સ્ટેક્ડ ટિકી અને ચમકતા કટદાણા.']
        ) + """

        <div class="callout callout-tip">
            <div class="callout-icon">💡</div>
            <div class="callout-content">
                <strong>બીડ્સ અને સિક્વિનના ૫ અતિ મહત્વના નિયમો:</strong>
                ૧. <b>Alt + CapsLock:</b> બીડ્સ કે સિક્વિનને <b>૯ ડિગ્રી</b> ના એંગલ પર સ્ટેપ-બાય-સ્ટેપ ફેરવી શકાય છે.<br/>
                ૨. <b>Fix Type 26:</b> ગોળ સિક્વિન માટે હંમેશા પેટર્ન 26 અથવા Triangle લોક વાપરો જેથી ટિકી ઊખડે નહીં.<br/>
                ૩. <b>Minimize Margin:</b> કિનારી પર અડધી ટિકી બહાર લટકતી હોય તો Minimize Margin થી તે આપોઆપ અંદર આવી જશે.<br/>
                ૪. <b>Short Stitches = 0.5 mm:</b> ખૂણા પર સોય બીડ્સની કાચની પાઇપ સાથે અથડાઈને ભાંગી ન જાય તે માટે શોર્ટ સ્ટીચ 0.5 mm સેટ રાખો.<br/>
                ૫. <b>Fix Adjust (Ctrl + A -> Stitch -> Fix Adjust):</b> ડિઝાઇન પૂરી થાય ત્યારે આ કમાન્ડ આપવાથી તમામ ઓવરલેપિંગ કાણાં સાફ થઈ જશે.
            </div>
        </div>
    </div>
    """

    
    sec12b = """
    <div class="section-card" id="sec-looping-chenille">
        <div class="section-header">
            <div class="section-title">
                <span>➰</span> Section 12B: Looping & Chenille (Moss / Terry) Embroidery Master Guide
            </div>
            <span class="section-tag">લૂપિંગ / ચેનીલ ફંદા એમ્બ્રોઇડરી માર્ગદર્શિકા</span>
        </div>
        <p style="margin-bottom: 16px;">
            સુરત અને ઇન્ટરનેશનલ માર્કેટમાં <b>લૂપિંગ (Looping), ચેનીલ (Chenille) અને મોસ સ્ટીચ (Moss Stitch / Terry Loop)</b> નું કામ 
            હાઇ-એન્ડ વેલ્વેટ લહેંગા, જેકેટ્સ અને કિડ્સ વેર માટે અત્યંત લોકપ્રિય છે. 
            સામાન્ય એમ્બ્રોઇડરીમાં દોરો કાપડની સપાટી પર સપાટ બેસે છે, જ્યારે લૂપિંગમાં દોરાના <b>૩D ઊભા લૂપ્સ (Upright Plush Loops)</b> બને છે જે ટવેલ અથવા વેલ્વેટ જેવો ભવ્ય લુક આપે છે.
        </p>

        <div class="guide-box">
            <h4>⚙️ લૂપિંગ મશીન મિકેનિઝમ અને સોફ્ટવેર કંટ્રોલ</h4>
            <p>
                <b>૧. હોલો નીડલ (Hollow Needle 120/19):</b> લૂપિંગ માટે ખાસ પોચી સોય વપરાય છે. સોયની અંદરથી જાડો ઊન કે એક્રેલિકનો ફ્લફી દોરો સતત પસાર થાય છે.<br/>
                <b>૨. રોટેટિંગ લૂપર હૂક (360° Looper Hook):</b> સોય કાપડની નીચે ઊતરે ત્યારે મશીનની નીચેનો લૂપર હૂક દોરાને પકડીને ૩૬૦ ડિગ્રી ગોળ ફરે છે અને ઉપર લૂપ છોડે છે.<br/>
                <b>૩. લૂપ હાઇટ સેટિંગ (Loop Height = 1.5mm થી 4.5mm):</b> EmCAD માં Chenille Property માં જઈ લૂપની ઊંચાઈ સેટ કરવામાં આવે છે. સ્ટાન્ડર્ડ વેલ્વેટ લુક માટે ૩.૦ mm બેસ્ટ છે.<br/>
                <b>૪. સ્પીડ કંટ્રોલ (RPM 400 - 600):</b> લૂપિંગ મશીન સામાન્ય એમ્બ્રોઇડરી જેટલી 1000 RPM સ્પીડે ચાલી શકતું નથી. દોરો તૂટી ન જાય તે માટે સ્પીડ ૫૦૦ RPM પર લોક કરવી.<br/>
                <b>૫. ટાઇ-ઓફ લોક (Chain Reverse 4 Stitches):</b> લૂપિંગ લાઇન પૂરી થતાં ૪ રિવર્સ ચેઈન સ્ટીચ આપવી ફરજિયાત છે જેથી પહેરતી વખતે લૂપ ખેંચાઈને ઉખડી ન જાય.
            </p>
        </div>

        <h3 style="color: var(--primary); margin: 24px 0 12px 0;">🎥 લૂપિંગ મોશન ગ્રાફિક્સ અને વેક્ટર સરખામણી</h3>
        <div class="anim-card">
            <div class="anim-card-header">
                <h4><span>➰</span> લૂપિંગ ચેનીલ સ્ટીચ મિકેનિઝમ (Looping / Chenille Simulation)</h4>
                <span class="badge-code">Hollow Needle + 360° Looper</span>
            </div>
            <div class="anim-container">
                <img src="emCad_organized_assets/anim_looping_chain_stitch.gif" alt="Looping Chain Stitch" loading="lazy">
            </div>
            <div class="anim-caption">
                <b>મશીન સિદ્ધાંત:</b> સોય કાપડની અંદર ઊતરે છે -> લૂપર હૂક દોરો પકડે છે -> સોય પાછી ઉપર આવે છે -> કાપડ પર 3D વેલ્વેટ લૂપ ઊભો રહે છે!
            </div>
        </div>

        """ + comparison_card(
            "75_Compare_Looping_Vector_Drawing_vs_Real_Embroidery.jpg",
            "લૂપિંગ સરખામણી: વેક્ટર પાથ & લૂપ હાઇટ vs વાસ્તવિક 3D વેલ્વેટ લૂપિંગ",
            "EmCAD Looping Vector vs Real 3D Velvet Chenille Garment",
            ['<b>Hollow Chenille Needle (પોચી હોલો સોય - 120/19):</b> સામાન્ય સોય કરતાં પોચી અને જાડી સોય જેની અંદરથી ઊન કે એક્રેલિકનો ફ્લફી દોરો પસાર થાય છે.', '<b>Rotating Looper Hook (લૂપર હૂક ૩૬૦°):</b> કાપડની નીચે આવેલો સ્પેશિયલ હૂક જે સોય નીચે ઊતરે ત્યારે દોરાને પકડીને લૂપ વણી લે છે.', '<b>Loop Height Setting (૧.૫ mm થી ૪.૫ mm):</b> સોફ્ટવેરમાં લૂપની ઊંચાઈ નક્કી થાય છે. ૩.૦ mm લૂપ હાઇટથી રોયલ પ્લશ ટેક્સચર મળે છે.', '<b>Loop Density & Underlay:</b> લૂપિંગ નીચે હળવો રનિંગ સ્ટીચ અંડરલે આપવો ફરજિયાત છે જેથી કાપડ ખેંચાઈને સંકોચાઈ ન જાય.', '<b>Reverse 4-Stitch Lock (ચેઈન રિવર્સ લૉક):</b> લૂપ પૂરું થતાં ૪ નાના ટાંકા રિવર્સ મારીને લૂપ બાંધવો પડે છે જેથી દોરો ખેંચાતાં ખુલી ન જાય.', '<b>Speed Limit (૪૦૦-૬૦૦ RPM):</b> લૂપિંગ મશીનને ૬૦૦ RPM થી વધુ સ્પીડે ચલાવવું નહીં, નહીંતર લૂપ તૂટી જાય છે.', '<b>Real Fabric Result (વાસ્તવિક કાપડ પરિણામ):</b> જમણી બાજુ રોયલ નેવી બ્લુ વેલ્વેટ પર ગોલ્ડન અને ક્રીમ ઊનના દોરાથી બનેલું આબેહૂબ મોસ/ચેનીલ 3D એમ્બ્રોઇડરી.']
        ) + """
    </div>
    """

    sec13 = """
    <div class="section-card" id="sec-locks">
        <div class="section-header">
            <div class="section-title">
                <span>🔒</span> Section 13: Step 13: Lock Methods & Thread Mechanics
            </div>
            <span class="section-tag">લોક પદ્ધતિ અને થ્રેડ કંટ્રોલ</span>
        </div>
        <p style="margin-bottom: 16px;">
            જો ડિઝાઇનમાં લોક ટાંકા (Tie-in / Tie-off) યોગ્ય ન હોય તો કાપડ ધોવાયા પછી કે પ્રેસ કરતી વખતે દોરો ઉકલી જશે અને ગ્રાહક માલ રિજેક્ટ કરશે.
        </p>

        <div class="image-gallery">
            """ + img_card("49_Step13_Lock_Method_Cording_Run_In_Out.jpg", "Step 13: લોક મેથડ & કોર્ડિંગ", "કોર્ડિંગ રન ઇન/આઉટ, સ્ટાર્ટ લોક અને એન્ડ ટાઇ-ઓફ") + """
            """ + img_card("50_Step13_Lock_Trim_Jump_Settings.jpg", "Step 13: લોક ટ્રીમ & જમ્પ સેટિંગ્સ", "કનેક્ટર મેનુ પેરામીટર્સ અને ઓટોમેટિક ટાઇ સ્ટીચ") + """
        </div>

        <table class="data-table">
            <thead><tr><th style="width: 200px;">લોક પ્રકાર</th><th>પદ્ધતિ અને મહત્વ</th></tr></thead>
            <tbody>
                <tr><td><b>Start Lock (Tie-In)</b></td><td>૩ થી ૫ ઝીણા ટાંકા આગળ-પાછળ ચાલીને ગાંઠ મારે છે જેથી ખેંચાતા દોરો નીકળી ન જાય.</td></tr>
                <tr><td><b>End Lock (Tie-Off)</b></td><td>ઓબ્જેક્ટ પૂરો થાય અને કાતર (Trim) ચાલે તે પહેલાં ૩-૪ ટાંકા મારીને દોરો પેક કરવો.</td></tr>
                <tr><td><b>Cording Lock</b></td><td>કોર્ડિંગ દોરીની શરૂઆત અને અંતમાં ૨-૩ mm આગળથી રન સ્ટીચ ચલાવીને દોરી દબાવવી.</td></tr>
                <tr><td><b>In / Out Connectors</b></td><td>Object Property -> Connectors માં જઈ હંમેશા Automatic Lock ઓન રાખવું.</td></tr>
            </tbody>
        </table>
    </div>
    """

    sec14 = """
    <div class="section-card" id="sec-dahao">
        <div class="section-header">
            <div class="section-title">
                <span>💾</span> Section 14: Step 14: File Formats (.DHP, .DST, .DHE) & Dahao Machine Setup
            </div>
            <span class="section-tag">ફાઇલ ફોર્મેટ્સ અને દહાઓ સેટિંગ</span>
        </div>
        <p style="margin-bottom: 16px;">
            પંચિંગ પત્યા પછી કઈ ફાઇલમાં સેવ કરવું અને દહાઓ મશીનના કમ્પ્યુટરમાં કયા સેટિંગ્સ કરવા તે નીચે મુજબ છે.
        </p>

        <div class="image-gallery">
            """ + img_card("51_Step14_File_Formats_DHP_DST_DHE_EMB.jpg", "Step 14: ફાઇલ ફોર્મેટ્સ તુલના", ".DHP, .DST, .DHE, .EMB અને સોફ્ટવેર કમ્પેટિબિલિટી") + """
            """ + img_card("52_Step14_Dahao_DST_Setting_Beads_Seq.jpg", "Step 14: દહાઓ DST સેટિંગ", "બીડ્સ અને સિક્વિન કમાન્ડ કોડ્સ કન્ફિગરેશન") + """
            """ + img_card("53_Dialog_Daho_Controller_Beads_Setting.jpg", "દહાઓ કંટ્રોલર ડાયલોગ", "Beads A, B, C, D અને Needle Assignment") + """
            """ + img_card("54_Step14_Daho_3Beads_4Beads_Combinations.jpg", "Step 14: ૩-બીડ્સ અને ૪-બીડ્સ કોમ્બિનેશન", "ABC, ABD, ACD કોમ્બિનેશન સેટિંગ") + """
            """ + img_card("55_Step14_Daho_Licensing_Versions_210_260.jpg", "Step 14: EmCAD વર્ઝન હિસ્ટ્રી", "v2.10, v2.60, v3.80 અને સિક્યુરિટી ડોંગલ") + """
        </div>

        <table class="data-table">
            <thead><tr><th style="width: 100px;">ફોર્મેટ</th><th style="width: 160px;">સિસ્ટમ પ્રકાર</th><th>લાક્ષણિકતાઓ અને ઉપયોગ</th></tr></thead>
            <tbody>
                <tr><td><span class="badge-code">.DHP</span></td><td><b>EmCAD Native ફાઇલ</b></td><td>ઓરિજિનલ માસ્ટર ફાઇલ. તમામ ઓબ્જેક્ટ્સ, નોડ્સ, પેરામીટર્સ અને પ્રોપર્ટીઝ એડિટેબલ રહે છે. હંમેશા આ ફાઇલ સાચવી રાખવી.</td></tr>
                <tr><td><span class="badge-code">.DST</span></td><td><b>Tajima Universal ફાઇલ</b></td><td>યુનિવર્સલ મશીન ફાઇલ. તેમાં માત્ર ટાંકા (Stitches), જમ્પ અને સ્ટોપ હોય છે. કોઈપણ બ્રાન્ડના મશીનમાં પેનડ્રાઇવથી ચાલે છે.</td></tr>
                <tr><td><span class="badge-code">.DHE / .DHA</span></td><td><b>Dahao Controller ફાઇલ</b></td><td>દહાઓ મશીનની ખાસ ફાઇલ જેમાં સિક્વિન, બીડ્સ અને કલર કોડ્સ ડાયરેક્ટ સપોર્ટ થાય છે. લેટેસ્ટ મધરબોર્ડમાં સીધી ચાલે છે.</td></tr>
                <tr><td><span class="badge-code">.EMB</span></td><td><b>Wilcom Software ફાઇલ</b></td><td>વિલકોમની ઓરિજિનલ ફાઇલ. <b>આ ફાઇલ સીધી EmCAD માં ખૂલતી નથી!</b> વિલકોમમાંથી .DST બનાવીને જ EmCAD માં લાવી શકાય.</td></tr>
            </tbody>
        </table>

        <div class="callout callout-tip">
            <div class="callout-icon">💡</div>
            <div class="callout-content">
                <strong>દહાઓ કંટ્રોલર ૩-બીડ્સ / ૪-બીડ્સ સેટિંગ:</strong>
                દહાઓ મશીનમાં જો ૪ બીડ્સ ડિવાઇસ લાગેલું હોય તો Seq A, Seq B, Seq AB અને Beads A, Beads B, Beads C, Beads D ના કોમ્બિનેશન્સ (ABC, ABD, ACD) કંટ્રોલરમાં સેટ થાય છે. ડિઝાઇન એક્સપોર્ટ કરતી વખતે Dahao Format પસંદ કરવાથી કોડ આપોઆપ ટ્રાન્સફર થાય છે.
            </div>
        </div>
    </div>
    """

    sec15 = """
    <div class="section-card" id="sec-saree">
        <div class="section-header">
            <div class="section-title">
                <span>🥻</span> Section 15: Step 15: Saree Punching & 25-Head Multi-Head Layout
            </div>
            <span class="section-tag">સાડી પંચિંગ અને ૨૫-હેડ મશીન</span>
        </div>
        <p style="margin-bottom: 16px;">
            સાડીનું પંચિંગ એ સુરત એમ્બ્રોઇડરી ઉદ્યોગનું સૌથી મોટું અને જવાબદારીભર્યું કામ છે. 
            ૨૫-હેડ વાળા વિશાળ મશીન પર સાડી બેસાડતી વખતે હેડ શિફ્ટ અને પલ્લુ મિરરિંગનું ખાસ ધ્યાન રાખવું પડે છે.
        </p>

        <div class="image-gallery">
            """ + img_card("56_Step15_Saree_400Area_Pally_Mirror.jpg", "Step 15: સાડી ૪૦૦ mm & પલ્લુ મિરર", "૪૦૦ mm એરિયા, ૧૧૨૦ mm હાઇટ અને પલ્લુ મિરર ૫૬૦ mm સેન્ટર") + """
            """ + img_card("57_Step15_Saree_Repeats_100_200_133.jpg", "Step 15: સાડી રીપીટ ગણતરી", "૧૦૦ mm (12 રીપીટ), ૨૦૦ mm (6 રીપીટ), ૧૩૩ mm (9 રીપીટ)") + """
            """ + img_card("58_Step15_25Head_Embroidery_Machine_Shift.jpg", "Step 15: ૨૫-હેડ મશીન શિફ્ટ", "હેડ ૧-૧૨ ડાબે, હેડ ૧૩ સેન્ટર, હેડ ૧૪-૨૫ જમણે") + """
            """ + img_card("59_Step15_MultiHead_Punching_Rules_AutoJump.jpg", "Step 15: મલ્ટી-હેડ પ્રોડક્શન નિયમો", "ઓટો જમ્પ, ટ્રાવેલ સ્ટીચ અને દોરો તૂટતો અટકાવવો") + """
            """ + img_card("60_Step15_Shading_Flower_Double_Shade.jpg", "Step 15: શેડિંગ ફ્લાવર ડબલ શેડ", "ગ્રેડિયન્ટ મિક્સિંગ અને સાડી બોર્ડર સેટિંગ") + """
        </div>

        <table class="data-table">
            <thead><tr><th style="width: 200px;">પેરામીટર</th><th>૨૫-હેડ મશીન પ્રોડક્શન નિયમ</th></tr></thead>
            <tbody>
                <tr><td><b>સાડી વર્કિંગ પહોળાઈ</b></td><td>400 mm મશીન ફ્રેમ (વાસ્તવિક પંચિંગ એરિયા 390 mm).</td></tr>
                <tr><td><b>સાડી વર્કિંગ ઊંચાઈ</b></td><td>1120 mm થી 1200 mm કુલ લંબાઈ.</td></tr>
                <tr><td><b>પલ્લુ મિરર પોઇન્ટ</b></td><td>560 mm બરાબર અડધા સેન્ટર પર પલ્લુ મિરર થાય છે.</td></tr>
                <tr><td><b>રીપીટ વિકલ્પો</b></td><td>100 mm (12 રીપીટ), 200 mm (6 રીપીટ), 133 mm (9 રીપીટ).</td></tr>
                <tr><td><b>૨૫-હેડ મશીન શિફ્ટ</b></td><td>હેડ ૧ થી ૧૨ ડાબી બાજુ, હેડ ૧૩ બરાબર મધ્યમાં (Center), હેડ ૧૪ થી ૨૫ જમણી બાજુ શિફ્ટ થાય છે.</td></tr>
                <tr><td><b>દોરો તૂટતો અટકાવવો</b></td><td>એક હેડ પર દોરો તૂટે તો આખા ૨૫ હેડ ઊભા રહી જાય છે! તેથી જમ્પ ઓછા અને ટ્રાવેલ રન સ્ટીચ વધુ વાપરવી.</td></tr>
            </tbody>
        </table>
    </div>
    """

    sec16 = """
    <div class="section-card" id="sec-finalize">
        <div class="section-header">
            <div class="section-title">
                <span>🏁</span> Section 16: Step 16: Production Finalize, Origin Lock & WhatsApp Approval
            </div>
            <span class="section-tag">ફાઇનલ પ્રોડક્શન ચેકલિસ્ટ</span>
        </div>
        <p style="margin-bottom: 16px;">
            ડિઝાઇન મશીન પર ચડાવતા પહેલાં અને પાર્ટીને મોકલતા પહેલાં આ ફાઇનલ ચેકલિસ્ટ પૂર્ણ કરવી ફરજિયાત છે.
        </p>

        <div class="image-gallery">
            """ + img_card("61_Step16_Design_Lock_DR250_Origin_Export.jpg", "Step 16: ઓરિજિન લોક DR 250", "ડિઝાઇન લોક DR 250 (X=0, Y=0) અને WhatsApp પ્રિવ્યુ") + """
            """ + img_card("66_Step16_F8_Break_Point_45Deg_PasteInPlace.jpg", "Step 16: F8 બ્રેક પોઇન્ટ & ૪૫° એંગલ", "F8 બ્રેક પોઇન્ટ અને પેસ્ટ ઇન પ્લેસ (Alt + Shift + V)") + """
            """ + img_card("67_Step16_Shortcuts_Summary_AltCapsLock_Rotate.jpg", "Step 16: શોર્ટકટ્સ સમરી", "Alt + CapsLock ૯ ડિગ્રી રોટેશન અને પ્રોડક્શન રૂલ્સ") + """
        </div>

        <div class="callout callout-danger">
            <div class="callout-icon">🚨</div>
            <div class="callout-content">
                <strong>ઓરિજિન લોક DR 250 (Origin Lock) કેમ ફરજિયાત છે?</strong>
                જો ઓરિજિન લોક નહીં કરો અને મશીન ઓપરેટર ભૂલથી ફ્રેમ થોડી પણ ખસેડશે, તો ૨૫ એ ૨૫ હેડની સોય ફ્રેમ સાથે અથડાશે (Frame Hit / Crash) અને હજારો રૂપિયાનું નુકસાન થશે. ડિઝાઇન પૂરી થયા પછી હંમેશા <b>Ctrl + Home</b> આપી <b>DR 250 (X=0, Y=0)</b> લોક કરો.
            </div>
        </div>

        <div class="callout callout-tip">
            <div class="callout-icon">💡</div>
            <div class="callout-content">
                <strong>WhatsApp પ્રિવ્યુ ટ્રીક:</strong>
                Print Preview સ્ક્રીનમાં જઈ બેકગ્રાઉન્ડ વ્હાઇટ કે બ્લેક કરી સ્ક્રિનશોટ લો. તેનાથી ગ્રાહકને ઓરિજિનલ એમ્બ્રોઇડરી જેવો 3D લુક દેખાશે અને ઓર્ડર તરત કન્ફર્મ થશે.
            </div>
        </div>
    </div>
    """

    

    sec_drive_gallery = """
    <div class="section-card" id="sec-drive-gallery">
        <div class="section-header">
            <div class="section-title">
                <span>🏭</span> Section 16B: Google Drive રીયલ ફેક્ટરી આર્કાઈવ & મશીન રેફરન્સ લાયબ્રેરી (37 Master Reference Swatches & Screens)
            </div>
            <span class="section-tag">૩૭ ઓરિજિનલ ફેક્ટરી સેમ્પલ્સ, મશીન હેડ્સ & emCAD Pro લૂપિંગ સ્ક્રીન્સ</span>
        </div>
        <p style="margin-bottom: 16px; font-size: 14.5px; line-height: 1.6;">
            આ સેક્શનમાં તમારા <b>Google Drive Download (20261010T063837Z-1-001)</b> માંથી મળેલા તમામ <b>૩૭ ઓરિજિનલ ઔદ્યોગિક સેમ્પલ્સ</b>, 
            Dahao emCAD Pro સોફ્ટવેરની લૂપિંગ અને સિક્વિન સ્ક્રીન્સ, મલ્ટી-હેડ મશીન પ્રોડક્શન ફોટોગ્રાફ્સ અને રીયલ એમ્બ્રોઇડરી ટેક્સચર્સને 
            વિસ્તૃત રીતે વર્ગીકૃત કરી દરેકનું પંચિંગ મહત્વ સમજાવવામાં આવ્યું છે:
        </p>

        <!-- SUB-SECTION 1: SOFTWARE UI & DIGITIZING -->
        <div style="background: #1E293B; border-radius: 10px; padding: 18px; margin-bottom: 24px; border: 1px solid #334155;">
            <h3 style="color: #38BDF8; margin-bottom: 10px; font-size: 16px;">
                🖥️ કેટેગરી ૧: Dahao emCAD Pro સોફ્ટવેર ઇન્ટરફેસ & ડિવાઇસ પેરામીટર્સ (૫ સ્ક્રીન્સ)
            </h3>
            <p style="color: #CBD5E1; font-size: 13.5px; margin-bottom: 14px;">
                આ સ્ક્રીનશોટ્સ Dahao emCAD 2.5 અને Enhanced 2.10 Pro ના વાસ્તવિક પંચિંગ વર્કસ્પેસ દર્શાવે છે.
            </p>
            <div class="image-gallery">
                """ + drv_img_card("DRV_13_EmCAD_Pro_2.10_Looping_Demo_Screen.jpg", "૧. emCAD Pro 2.10 - LOOPING_DEMO.DHP", "લૂપિંગ ડેમો ફાઇલ! Sequin B (32.2mm) ફીડિંગ, નીડલ બાર્સ, ટ્રાવેલ અને ટાકા પેરામીટર્સ.") + """
                """ + drv_img_card("DRV_14_EmCAD_Pro_Sequin_B_Device_Params.jpg", "૨. Sequin B ડિવાઇસ પેરામીટર્સ ક્લોઝ-અપ", "X: 1.15 mm, Y: 0.00 mm, ડિવાઇસ ડ્રોપ અંતર અને ટાકા લોકિંગ પોઝિશન.") + """
                """ + drv_img_card("DRV_03_EmCAD_2.5_Software_Interface.jpg", "૩. Dahao emCAD 2.5 વર્કસ્પેસ UI", "કોઓર્ડિનેટ્સ X=-75.06, Y=-75.78, L=106.66 mm, 5 નીડલ કલર પેલેટ અને ટૂલબાર્સ.") + """
                """ + drv_img_card("DRV_35_Fill_vs_Outline_Stitch_Types_Chart.jpg", "૪. Fill Stitches vs Outline Stitches ચાર્ટ", "તતામી, સાટિન, કોન્ટૂર, ફ્લોરેન્ટાઇન ફિલ vs રન, ઝિગઝેગ, E-Stitch અને મોટિફ આઉટલાઇન.") + """
                """ + drv_img_card("DRV_23_Stitch_Density_Punching_Dialog.jpg", "૫. સ્ટીચ ડેન્સિટી & ઓબ્જેક્ટ પ્રોપર્ટી ડાયલોગ", "સાટિન ઘનતા 0.38-0.42 mm, તતામી લંબાઈ 3.8 mm અને અન્ડરલે કંટ્રોલ પેનલ.") + """
            </div>
            <div style="background: rgba(56, 189, 248, 0.1); border-left: 4px solid #38BDF8; padding: 10px 14px; margin-top: 12px; border-radius: 4px; font-size: 13px; color: #E2E8F0;">
                <b>💡 ટેકનિકલ ટિપ:</b> DRV_13 સ્ક્રીન સાબિત કરે છે કે લૂપિંગ અને સિક્વિન ડિવાઇસ B માટે મશીન ફીડિંગ પેરામીટર <b>32.2 mm</b> રાખવામાં આવે છે, જેથી ડિવાઇસ ફેબ્રિક પર અથડાયા વગર સ્મૂધ સિક્વિન/લૂપ ડ્રોપ કરી શકે.
            </div>
        </div>

        <!-- SUB-SECTION 2: INDUSTRIAL EMBROIDERY MACHINES -->
        <div style="background: #1E293B; border-radius: 10px; padding: 18px; margin-bottom: 24px; border: 1px solid #334155;">
            <h3 style="color: #4ADE80; margin-bottom: 10px; font-size: 16px;">
                🏭 કેટેગરી ૨: ઇન્ડસ્ટ્રિયલ મલ્ટી-હેડ પ્રોડક્શન મશીનરી & નીડલ હેડ્સ (૨ ફોટોઝ)
            </h3>
            <p style="color: #CBD5E1; font-size: 13.5px; margin-bottom: 14px;">
                કારખાનામાં મોટા પાયે સાડી, લેસ અને ડ્રેસ મટીરીયલ બનાવવા વપરાતા ૨૫ થી ૩૨ હેડ મલ્ટી-હેડ મશીન્સ.
            </p>
            <div class="image-gallery">
                """ + drv_img_card("DRV_01_MultiHead_Embroidery_Machine_Shop.jpg", "૬. ૨૫/૩૦ હેડ મલ્ટી-હેડ પ્રોડક્શન ફ્લોર", "મોટી ફ્રેમ પર એકસાથે ૨૫ હેડ સાડી પ્રોડક્શન, ઓટો-શિફ્ટ અને ફેબ્રિક ટેન્શન રોલર્સ.") + """
                """ + drv_img_card("DRV_29_Barudan_Machine_Head_Needle_Bar.jpg", "૭. Barudan / Dahao ઇન્ડસ્ટ્રિયલ હેડ આર્કિટેક્ચર", "નીડલ બાર મિકેનિઝમ, થ્રેડ ટેન્શન સ્પ્રિંગ્સ, ટેક-અપ લિવર અને ઓટો-ટ્રિમર કટર બ્લોક.") + """
            </div>
            <div style="background: rgba(74, 222, 128, 0.1); border-left: 4px solid #4ADE80; padding: 10px 14px; margin-top: 12px; border-radius: 4px; font-size: 13px; color: #E2E8F0;">
                <b>⚙️ પ્રોડક્શન નિયમ:</b> ૨૫-હેડ મશીનમાં હેડ-ટુ-હેડ સ્પેસિંગ (Head Distance) ચોક્કસ <b>300 mm</b> અથવા <b>400 mm</b> હોય છે. પંચિંગ કરતી વખતે ડિઝાઇન રિપીટ આ અંતર સાથે 100% મેચ થવી જોઈએ.
            </div>
        </div>

        <!-- SUB-SECTION 3: CORDING & DORI WORK -->
        <div style="background: #1E293B; border-radius: 10px; padding: 18px; margin-bottom: 24px; border: 1px solid #334155;">
            <h3 style="color: #F59E0B; margin-bottom: 10px; font-size: 16px;">
                🧵 કેટેગરી ૩: કોર્ડિંગ & દોરી એમ્બ્રોઇડરી ટેકનીક્સ (૫ સેમ્પલ્સ)
            </h3>
            <p style="color: #CBD5E1; font-size: 13.5px; margin-bottom: 14px;">
                જાડી દોરી, ગોલ્ડ ઝરી કોર્ડ અને યાર્નને ફેબ્રિક પર ઝિગઝેગ કે રન સ્ટીચ વડે બાંધવાની માસ્ટર ટેકનીક્સ.
            </p>
            <div class="image-gallery">
                """ + drv_img_card("DRV_12_Heavy_Gold_Cording_Dori_Stitch.jpg", "૮. હેવી ગોલ્ડ દોરી (Cording Dori) વર્ક", "જાડી સોનેરી દોરી પર ૧.૨ mm ઝિગઝેગ ટાંકા સાથે નેકલાઇન આઉટલાઇન.") + """
                """ + drv_img_card("DRV_19_Thick_Cording_Rope_Zigzag_Lock.jpg", "૯. થીક રોપ કોર્ડિંગ & ઝિગઝેગ ટેકડાઉન", "હાઇ-વોલ્યુમ રોપ દોરી પર ૨.૫ mm ઝિગઝેગ લિગામેન્ટ લોક ટાંકા.") + """
                """ + drv_img_card("DRV_25_MultiColor_Cording_Yarn_Mesh.jpg", "૧૦. મલ્ટી-કલર કોર્ડિંગ યાર્ન નેટ વર્ક", "નેટ જાળી પર અલગ-અલગ રંગની દોરીઓનું મલ્ટી-લેયર કમ્પોઝિશન.") + """
                """ + drv_img_card("DRV_32_Island_Cording_Dori_Border.jpg", "૧૧. આઇલેન્ડ કોર્ડિંગ દોરી બોર્ડર", "કટિંગ વગર સળંગ દોરી ફેરવવા માટે આઇલેન્ડ કનેક્ટર અને સેન્ટર ટ્રાવેલ.") + """
                """ + drv_img_card("DRV_11_Gold_Thread_Relief_Work.jpg", "૧૨. ગોલ્ડ થ્રેડ રિલિફ અને દોરી હાઇલાઇટ્સ", "પાઘડી સાટિન સાથે દોરીની સુંદર બોર્ડર બનાવવાની જુગલબંધી.") + """
            </div>
            <div style="background: rgba(245, 158, 11, 0.1); border-left: 4px solid #F59E0B; padding: 10px 14px; margin-top: 12px; border-radius: 4px; font-size: 13px; color: #E2E8F0;">
                <b>⚠️ પંચિંગ સાવચેતી:</b> દોરીમાં ક્યારેય શાર્પ 90° ખૂણો ન મૂકવો. હંમેશા <b>1.5 થી 2 mm નું સ્મૂધ રેડિયસ કર્વ</b> આપવું જેથી દોરી ડિવાઇસમાં ફસાય નહીં.
            </div>
        </div>

        <!-- SUB-SECTION 4: LOOPING & CHENILLE EMBROIDERY -->
        <div style="background: #1E293B; border-radius: 10px; padding: 18px; margin-bottom: 24px; border: 1px solid #334155;">
            <h3 style="color: #EC4899; margin-bottom: 10px; font-size: 16px;">
                ➰ કેટેગરી ૪: લૂપિંગ & ચેનીલ એમ્બ્રોઇડરી ટેક્સચર્સ (૩ સેમ્પલ્સ)
            </h3>
            <p style="color: #CBD5E1; font-size: 13.5px; margin-bottom: 14px;">
                સોફ્ટ ટેરી-ટોવેલ જેવી લૂપ પાઇલ અને ચેઇન સ્ટીચિંગ વડે બનાવવામાં આવતી પ્રીમિયમ લૂપિંગ ઇફેક્ટ.
            </p>
            <div class="image-gallery">
                """ + drv_img_card("DRV_16_Chenille_Looping_Art_Embroidery.jpg", "૧૩. આર્ટ એમ્બ્રોઇડરી લૂપિંગ પાઇલ", "ઉપસેલા લૂપ્સ વડે બનાવેલું પ્રીમિયમ 3D ચેનીલ ટેક્સચર.") + """
                """ + drv_img_card("DRV_02_Loop_Chain_Chenille_Embroidery_Sample.jpg", "૧૪. ચેઇન સ્ટીચ લૂપિંગ કોન્ટૂર", "સળંગ ચેઇન લૂપ્સ વડે બોર્ડર અને પેટલ ફિલિંગનું સેમ્પલ.") + """
                """ + drv_img_card("DRV_22_Pudder_Pela_Albe_Stitch_Types.jpg", "૧૫. પુડ્ડર / પેલા / આલ્બે સ્ટીચ વેરાયટી", "પરંપરાગત ટેક્સચર સ્ટીચ ટાઇપ્સ: પુડ્ડર લૂપ અને પેલા રિલિફ સ્ટીચિંગ.") + """
            </div>
            <div style="background: rgba(236, 72, 153, 0.1); border-left: 4px solid #EC4899; padding: 10px 14px; margin-top: 12px; border-radius: 4px; font-size: 13px; color: #E2E8F0;">
                <b>🔒 લૂપિંગ લોક નિયમ:</b> લૂપ સ્ટીચ પાછળથી ખુલી ન જાય તે માટે શરૂઆતમાં અને છેડે <b>૩ થી ૪ નોર્મલ લોક ટાંકા (Tie-in/Tie-off)</b> મૂકવા અનિવાર્ય છે.
            </div>
        </div>

        <!-- SUB-SECTION 5: BEADS & PEARLS WORK -->
        <div style="background: #1E293B; border-radius: 10px; padding: 18px; margin-bottom: 24px; border: 1px solid #334155;">
            <h3 style="color: #A855F7; margin-bottom: 10px; font-size: 16px;">
                ⚪ કેટેગરી ૫: બીડ્સ & મોતી એમ્બ્રોઇડરી માસ્ટરી (૬ સેમ્પલ્સ)
            </h3>
            <p style="color: #CBD5E1; font-size: 13.5px; margin-bottom: 14px;">
                ૨.૦ mm થી ૪.૦ mm ના કાચના મોતી અને પર્લ્સને ૪૫° ખૂણે લોક ટાંકા સાથે ટાંકીને બનાવેલા ઓરિજિનલ સેમ્પલ્સ.
            </p>
            <div class="image-gallery">
                """ + drv_img_card("DRV_10_Crystal_Beads_Hand_Machine_Khaka.jpg", "૧૬. ક્રિસ્ટલ બીડ્સ & હેન્ડ-લુક ખાકા", "હસ્તકલા જેવો લુક આપતા મશીન બીડ્સ પ્લેસમેન્ટ અને ઝીણા મોતી.") + """
                """ + drv_img_card("DRV_21_Gold_Beads_45Deg_Taka_Embroidery.jpg", "૧૭. ગોલ્ડ બીડ્સ ૪૫° ટાંકા લોકિંગ", "ચોક્કસ ૪૫ ડિગ્રી એંગલે ક્રોસ ટાંકો જેથી સોય મોતીની ધારે અથડાય નહીં.") + """
                """ + drv_img_card("DRV_15_MultiSize_Pearl_Beads_Embroidery.jpg", "૧૮. મલ્ટી-સાઇઝ પર્લ બીડ્સ કોમ્બો", "મોટા (૩.૫ mm) અને નાના (૨.૦ mm) મોતીનું સુંદર મિશ્રણ.") + """
                """ + drv_img_card("DRV_20_Micro_Beads_Angle_Taka_Detail.jpg", "૧૯. માઇક્રો બીડ્સ એંગલ વિગતો", "Alt + CapsLock કીબોર્ડ શોર્ટકટ વડે ૯° ના ગુણકમાં મોતી ફેરવવાની રીત.") + """
                """ + drv_img_card("DRV_34_Curved_Contour_Beads_Placement.jpg", "૨૦. કર્વ્ડ કોન્ટૂર બીડ્સ પ્લેસમેન્ટ", "તીક્ષ્ણ વળાંક પર મોતીઓ વચ્ચે ઓવરલેપ રોકવા માટે સ્ટેપ સ્પેસિંગ.") + """
                """ + drv_img_card("DRV_37_Sequin_Beads_Combo_Lace_Border.jpg", "૨૧. સિક્વિન + બીડ્સ કોમ્બો લેસ બોર્ડર", "સિક્વિન અને મોતીની સંયુક્ત લેસ ડિઝાઇન વિથ ઝીરો જમ્પ.") + """
            </div>
            <div style="background: rgba(168, 85, 247, 0.1); border-left: 4px solid #A855F7; padding: 10px 14px; margin-top: 12px; border-radius: 4px; font-size: 13px; color: #E2E8F0;">
                <b>🎯 બીડ્સ ગણતરી:</b> ૨.૫ mm ના મોતી માટે પંચિંગ ટાંકો = <b>૨.૮ mm</b> રાખવો. ૩.૦ mm ના મોતી માટે ટાંકો = <b>૩.૩ mm</b> રાખવો (+0.3 mm ક્લિયરન્સ).
            </div>
        </div>

        <!-- SUB-SECTION 6: SEQUIN & PAILLETTES -->
        <div style="background: #1E293B; border-radius: 10px; padding: 18px; margin-bottom: 24px; border: 1px solid #334155;">
            <h3 style="color: #06B6D4; margin-bottom: 10px; font-size: 16px;">
                ✨ કેટેગરી ૬: સિક્વિન / સિતારા એમ્બ્રોઇડરી ટેકનીક્સ (૪ સેમ્પલ્સ)
            </h3>
            <p style="color: #CBD5E1; font-size: 13.5px; margin-bottom: 14px;">
                સપાટ સિતારા, ઓવરલેપિંગ સ્કેલ અને સિક્વિન ઉપર મોતી (Double Stack) ના માસ્ટર સેમ્પલ્સ.
            </p>
            <div class="image-gallery">
                """ + drv_img_card("DRV_07_Sequin_Overlapping_Scale_Border.jpg", "૨૨. ઓવરલેપિંગ સિક્વિન સ્કેલ બોર્ડર", "મચ્છી સ્કેલ પદ્ધતિ: એક સિતારો બીજા સિતારા પર ૫૦% ઓવરલેપ થઈને લોક થાય છે.") + """
                """ + drv_img_card("DRV_04_Sequin_Rosette_Circular_Pattern.jpg", "૨૩. ગોળ ચક્રી સિક્વિન રોઝેટ મોટિફ", "સર્ક્યુલર એંગલમાં ઘૂમતા સિતારા વિથ સેન્ટ્રલ લોક સ્ટીચ.") + """
                """ + drv_img_card("DRV_27_Double_Stack_Sequin_Beads_Pattern.jpg", "૨૪. ડબલ સ્ટેક સિક્વિન + બીડ્સ સ્વેચ", "નીચે સિતારો અને ઉપર મોતીનો કુંભી ટાંકો (Double Stack Luxury Stitch).") + """
                """ + drv_img_card("DRV_28_Double_Stack_Sequin_Beads_Pattern_Var.jpg", "૨૫. ડબલ સ્ટેક વેરીએશન ડિઝાઇન", "અલગ કલરના ફેબ્રિક પર ડબલ સ્ટેક સિતારા-મોતીની રોયલ બોર્ડર.") + """
            </div>
            <div style="background: rgba(6, 182, 212, 0.1); border-left: 4px solid #06B6D4; padding: 10px 14px; margin-top: 12px; border-radius: 4px; font-size: 13px; color: #E2E8F0;">
                <b>📐 સિક્વિન સ્પેસિંગ:</b> ૫ mm સિક્વિન માટે મચ્છી સ્કેલ સ્પેસિંગ = <b>૨.૫ mm</b>. સિંગલ ફ્લેટ સિક્વિન માટે સ્પેસિંગ = <b>૫.૫ mm</b>.
            </div>
        </div>

        <!-- SUB-SECTION 7: PAGHDI & SATIN RELIEF -->
        <div style="background: #1E293B; border-radius: 10px; padding: 18px; margin-bottom: 24px; border: 1px solid #334155;">
            <h3 style="color: #EAB308; margin-bottom: 10px; font-size: 16px;">
                👑 કેટેગરી ૭: પાઘડી & સાટિન સ્ટીચ રિલિફ વર્ક (૪ સેમ્પલ્સ)
            </h3>
            <p style="color: #CBD5E1; font-size: 13.5px; margin-bottom: 14px;">
                ઊંડાણ અને 3D ઉપસેલો લુક આપતા પાઘડી સ્ટીચ અને સાટિન કોલમ્સ.
            </p>
            <div class="image-gallery">
                """ + drv_img_card("DRV_08_Paghdi_Satin_Floral_Embroidery.jpg", "૨૬. હાઇ-ડેન્સિટી પાઘડી ફ્લાવર", "સાટિન પાઘડી સ્ટીચ વડે બનાવેલી ઉપસેલી પાંખડીઓ.") + """
                """ + drv_img_card("DRV_18_Paghdi_Contour_Satin_Relief.jpg", "૨૭. પાઘડી કોન્ટૂર સાટિન રિલિફ", "વળાંકવાળી બોર્ડર પર વળાંક મુજબ ફરતા સાટિન ટાંકા.") + """
                """ + drv_img_card("DRV_26_Dense_Satin_Tatami_Split_Work.jpg", "૨૮. સાટિન + તતામી સ્પ્લિટ રિલિફ", "૮ mm થી પહોળા ભાગમાં દોરાને તૂટતો રોકવા માટે વચ્ચે તતામી સ્પ્લિટ.") + """
                """ + drv_img_card("DRV_31_Architectural_Satin_Column_Motif.jpg", "૨૯. આર્કિટેક્ચરલ સાટિન કોલમ મોટિફ", "જિયોમેટ્રિક સ્તંભ અને શાર્પ કોર્નર્સ સાથે મજબૂત પાઘડી સ્ટીચ.") + """
            </div>
            <div style="background: rgba(234, 179, 8, 0.1); border-left: 4px solid #EAB308; padding: 10px 14px; margin-top: 12px; border-radius: 4px; font-size: 13px; color: #E2E8F0;">
                <b>⚡ પાઘડી સિક્રેટ:</b> F4 પાઘડી ટૂલ વાપરતી વખતે હંમેશા નીચે <b>Edge Run Underlay</b> મૂકવો જેથી પાઘડીની કિનારી શાર્પ અને કાપડ સંકોચાય નહીં.
            </div>
        </div>

        <!-- SUB-SECTION 8: SHADING, VECTORS & MIRROR WORK -->
        <div style="background: #1E293B; border-radius: 10px; padding: 18px; margin-bottom: 24px; border: 1px solid #334155;">
            <h3 style="color: #10B981; margin-bottom: 10px; font-size: 16px;">
                🌸 કેટેગરી ૮: વેક્ટર ડ્રોઇંગ, શેડિંગ & મિરર વર્ક (૮ સેમ્પલ્સ)
            </h3>
            <p style="color: #CBD5E1; font-size: 13.5px; margin-bottom: 14px;">
                રિયલ ગ્લાસ આભલા, વેક્ટર આઉટલાઇનિંગ, કોઈલ સ્ટીચ અને ફ્લોરેન્ટાઇન કર્વ્ડ ઇફેક્ટ્સ.
            </p>
            <div class="image-gallery">
                """ + drv_img_card("DRV_33_Mirror_Work_Glass_Embroidery.jpg", "૩૦. રિયલ મિરર (આભલા) ગ્લાસ એમ્બ્રોઇડરી", "કાચના આભલાને પકડી રાખતી અષ્ટકોણીય સાટિન ફ્રેમ વિથ ઝીરો સ્ક્રેચ.") + """
                """ + drv_img_card("DRV_06_Star_Motif_Gradient_Stitch.jpg", "૩૧. મલ્ટી-શેડેડ સ્ટાર મોટિફ", "બે રંગના દોરાનું કુદરતી મિશ્રણ (Color Gradient Shading).") + """
                """ + drv_img_card("DRV_24_Spiral_Coil_Lollipop_Stitch.jpg", "૩૨. સ્પાયરલ કોઈલ / લોલીપોપ સ્ટીચ", "ગોળ ઘૂમતી સર્પાકાર સ્ટીચ પેટર્ન વિથ સેન્ટ્રલ એન્કર.") + """
                """ + drv_img_card("DRV_30_Florentine_Cross_Stitch_Swatch.jpg", "૩૩. ફ્લોરેન્ટાઇન કર્વ્ડ & ક્રોસ સ્ટીચ", "પાણીના મોજાં જેવી ફ્લોરેન્ટાઇન વળાંકવાળી સ્ટીચ લાઇન.") + """
                """ + drv_img_card("DRV_05_Tatami_Mesh_Grid_Background.jpg", "૩૪. તતામી મેશ ગ્રીડ બેકગ્રાઉન્ડ", "કાપડને ખેંચાતું રોકવા માટે અન્ડરલે જાળી નેટવર્ક.") + """
                """ + drv_img_card("DRV_09_Floral_Vector_Punching_Drawing.jpg", "૩૫. પંચિંગ વેક્ટર ફ્લાવર ડ્રોઇંગ", "સ્કેન ઈમેજ પરથી શુદ્ધ વેક્ટર લાઈન્સ બનાવવાનું ડ્રોઇંગ સ્ટેજ.") + """
                """ + drv_img_card("DRV_17_Geometric_Run_Outline_Drawing.jpg", "૩૬. જિયોમેટ્રિક રન સ્ટીચ આઉટલાઇન", "બોર્ડર્સ અને ગાઈડલાઈન્સ માટે ચોક્કસ રન સ્ટીચ પાથ.") + """
                """ + drv_img_card("DRV_36_Vector_Flower_Punching_Artwork.jpg", "૩૭. કલર્ડ આર્ટવર્ક પ્લાનિંગ શીટ", "પંચિંગ શરૂ કરતાં પહેલાં નીડલ કલર સિક્વન્સ અને રૂટીંગ પ્લાનિંગ.") + """
            </div>
            <div style="background: rgba(16, 185, 129, 0.1); border-left: 4px solid #10B981; padding: 10px 14px; margin-top: 12px; border-radius: 4px; font-size: 13px; color: #E2E8F0;">
                <b>🪞 આભલા માસ્ટરી:</b> મિરર વર્કમાં પહેલાં <b>Inner Hexagon Run Underlay</b> મૂકો જેથી કાચ બેસી જાય, ત્યારબાદ ઉપર <b>Overcast Satin = 0.35 mm</b> ઘનતાથી લોક કરો.
            </div>
        </div>

        <!-- SUMMARY REFERENCE TABLE -->
        <div style="margin-top: 24px;">
            <h3 style="color: var(--primary); margin-bottom: 12px;">📊 ૩૭ ડ્રાઇવ રેફરન્સ એસેટ્સ - ત્વરિત ટેકનિકલ સારાંશ કોષ્ટક</h3>
            <table class="data-table">
                <thead>
                    <tr>
                        <th>નંબર</th>
                        <th>ફાઇલ નામ</th>
                        <th>કેટેગરી & વિષય</th>
                        <th>EmCAD ટૂલ</th>
                        <th>મશીન પેરામીટર / સાવચેતી</th>
                    </tr>
                </thead>
                <tbody>
                    <tr><td>૦૧</td><td>DRV_13</td><td>emCAD Pro 2.10 Looping Screen</td><td>Looping / Sequin B</td><td>Feed: 32.2 mm, Spacing: 1.15 mm</td></tr>
                    <tr><td>૦૨</td><td>DRV_14</td><td>Sequin B Device Close-up</td><td>Device Parameters</td><td>X: 1.15 mm, Y: 0.00 mm, Tie: 2 Stitches</td></tr>
                    <tr><td>૦૩</td><td>DRV_03</td><td>emCAD 2.5 Workspace UI</td><td>Standard Digitizing</td><td>Needle selection, Zoom 1.00, Ruler mm</td></tr>
                    <tr><td>૦૪</td><td>DRV_35</td><td>Fill vs Outline Stitch Chart</td><td>F3 Tatami / F2 Satin</td><td>Density 0.40 mm, Stitch Length 3.8 mm</td></tr>
                    <tr><td>૦૫</td><td>DRV_23</td><td>Stitch Density Dialog</td><td>Object Properties</td><td>Underlay, Pull Compensation +0.15 mm</td></tr>
                    <tr><td>૦૬</td><td>DRV_01</td><td>Multi-Head Machine Shop</td><td>Factory Production</td><td>25-Head, Repeat Spacing 300/400 mm</td></tr>
                    <tr><td>૦૭</td><td>DRV_29</td><td>Barudan Machine Head</td><td>Hardware Mechanics</td><td>Thread tension, Auto-trimmer, Needles</td></tr>
                    <tr><td>૦૮</td><td>DRV_12</td><td>Heavy Gold Cording Work</td><td>F11 / F12 Cording</td><td>Zigzag width: 1.2 mm, Length: 1.8 mm</td></tr>
                    <tr><td>૦૯</td><td>DRV_19</td><td>Thick Rope Zigzag Lock</td><td>Rope Cording</td><td>Tackdown pitch: 2.5 mm, Smooth radius</td></tr>
                    <tr><td>૧૦</td><td>DRV_25</td><td>Multi-Color Cording Mesh</td><td>Yarn Embroidery</td><td>Needle clearance, Low machine speed</td></tr>
                    <tr><td>૧૧</td><td>DRV_32</td><td>Island Cording Dori Border</td><td>Island Cord Tool</td><td>Continuous feed, Zero internal trims</td></tr>
                    <tr><td>૧૨</td><td>DRV_11</td><td>Gold Thread Relief Work</td><td>Satin + Cording</td><td>Dual texture elevation</td></tr>
                    <tr><td>૧૩</td><td>DRV_16</td><td>Chenille Looping Art Swatch</td><td>Looping / Chenille</td><td>Loop pile height: 2.0 mm, Soft yarn</td></tr>
                    <tr><td>૧૪</td><td>DRV_02</td><td>Loop Chain Stitch Sample</td><td>Chain Stitching</td><td>Loop density 0.50 mm, Tie-in lock</td></tr>
                    <tr><td>૧૫</td><td>DRV_22</td><td>Pudder / Pela / Albe Stitches</td><td>Specialty Stitches</td><td>Textured background fill</td></tr>
                    <tr><td>૧૬</td><td>DRV_10</td><td>Crystal Beads Hand-Look</td><td>F7 Beads Digitizing</td><td>Glass crystal beads, 45° cross lock</td></tr>
                    <tr><td>૧૭</td><td>DRV_21</td><td>Gold Beads 45° Taka</td><td>Beads Angle Lock</td><td>45° Angle taka, Taka length: 2.8 mm</td></tr>
                    <tr><td>૧૮</td><td>DRV_15</td><td>Multi-Size Pearl Combo</td><td>Dual Bead Heads</td><td>Combo 2.0 mm + 3.5 mm pearls</td></tr>
                    <tr><td>૧૯</td><td>DRV_20</td><td>Micro Beads Angle Detail</td><td>Alt + CapsLock</td><td>Rotate 9° increments, Precise clearance</td></tr>
                    <tr><td>૨૦</td><td>DRV_34</td><td>Curved Contour Beads</td><td>Contour Bead Flow</td><td>Slow feed around sharp curves</td></tr>
                    <tr><td>૨૧</td><td>DRV_37</td><td>Sequin + Beads Combo Lace</td><td>Hybrid Devices</td><td>Sequin base + Pearl center lock</td></tr>
                    <tr><td>૨૨</td><td>DRV_07</td><td>Overlapping Scale Sequin</td><td>Fish Scale Sequin</td><td>Pitch: 2.5 mm (50% overlap of 5mm)</td></tr>
                    <tr><td>૨૩</td><td>DRV_04</td><td>Circular Sequin Rosette</td><td>Radial Sequin</td><td>Center anchor stitch, Radial feed</td></tr>
                    <tr><td>૨૪</td><td>DRV_27</td><td>Double Stack Sequin + Beads</td><td>Stacked Device</td><td>5mm Cup sequin + 3mm Pearl stack</td></tr>
                    <tr><td>૨૫</td><td>DRV_28</td><td>Double Stack Variation</td><td>Luxury Border</td><td>High-end bridal lace embroidery</td></tr>
                    <tr><td>૨૬</td><td>DRV_08</td><td>Paghdi Satin Floral Work</td><td>F4 Paghdi Column</td><td>High-density 3D column, Density 0.38</td></tr>
                    <tr><td>૨૭</td><td>DRV_18</td><td>Paghdi Contour Relief</td><td>Turning Satin</td><td>Turning angle lines, Smooth curve flow</td></tr>
                    <tr><td>૨૮</td><td>DRV_26</td><td>Dense Satin Tatami Split</td><td>Pattern Split</td><td>Prevent long floats > 8mm via Tatami</td></tr>
                    <tr><td>૨૯</td><td>DRV_31</td><td>Architectural Satin Columns</td><td>Column Digitizing</td><td>Edge run underlay, Crisp corner cuts</td></tr>
                    <tr><td>૩૦</td><td>DRV_33</td><td>Real Glass Mirror Work</td><td>Mirror Frame Tool</td><td>Octagonal cage stitch, Overcast 0.35 mm</td></tr>
                    <tr><td>૩૧</td><td>DRV_06</td><td>Star Motif Color Gradient</td><td>Color Blending</td><td>Two-tone density feathering</td></tr>
                    <tr><td>૩૨</td><td>DRV_24</td><td>Spiral Coil Lollipop Stitch</td><td>Coil Stitch Run</td><td>Continuous spiral path, Inward travel</td></tr>
                    <tr><td>૩૩</td><td>DRV_30</td><td>Florentine & Cross Stitch</td><td>Wave Effect Fill</td><td>Curved wave lines across object</td></tr>
                    <tr><td>૩૪</td><td>DRV_05</td><td>Tatami Mesh Grid Network</td><td>Grid Underlay</td><td>Stabilize delicate sheer fabrics</td></tr>
                    <tr><td>૩૫</td><td>DRV_09</td><td>Vector Flower Punch Drawing</td><td>H Shape Edit</td><td>Clean node placement before punching</td></tr>
                    <tr><td>૩૬</td><td>DRV_17</td><td>Geometric Run Outline Path</td><td>Run Stitch (F6)</td><td>Path routing, Minimize machine jumps</td></tr>
                    <tr><td>૩૭</td><td>DRV_36</td><td>Color Artwork Planning Sheet</td><td>Sequence Planning</td><td>Pre-production colorway mapping</td></tr>
                </tbody>
            </table>
        </div>
    </div>
    """

    sec_troubleshooting = """
    <div class="section-card" id="sec-troubleshooting">
        <div class="section-header">
            <div class="section-title">
                <span>🛠️</span> Section 17A: Common Mistakes & Instant Troubleshooting Matrix
            </div>
            <span class="section-tag">વારંવાર થતી ૧૦ ભૂલો અને તેના ઉકેલો</span>
        </div>
        <p style="margin-bottom: 16px;">
            ફેક્ટરીમાં પંચિંગ ડિઝાઇનમાં કોઈ ભૂલ હોય ત્યારે મશીન પર પ્રોડક્શન અટકી જાય છે અને માલિકનું મોટું નુકસાન થાય છે. 
            નીચે એમ્બ્રોઇડરી પ્રોડક્શનની ટોપ ૧૦ સમસ્યાઓ, તેના ચોક્કસ કારણો અને EmCAD માં ૧-ક્લિક ઉકેલો આપેલા છે:
        </p>

        <table class="data-table">
            <thead>
                <tr>
                    <th style="width: 150px;">સમસ્યા (Problem)</th>
                    <th style="width: 180px;">લક્ષણ (Symptom on Machine)</th>
                    <th>મૂળ કારણ (Root Cause)</th>
                    <th style="width: 260px;">EmCAD સોફ્ટવેર ઉકેલ (1-Click Fix)</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><b>૧. દોરો વારંવાર તૂટે છે (Thread Breakage)</b></td>
                    <td>મશીન દર ૨ મિનિટે ઊભું રહી જાય છે.</td>
                    <td>ટાંકાની ઘનતા વધુ પડતી ઘાટી (Density &lt; 0.35 mm) છે અથવા તીવ્ર વળાંક પર ટાંકા ગૂંચવાય છે.</td>
                    <td>Density વધારીને <b>0.45 mm</b> કરો અને Object Property માં <b>Short Stitches = 0.5 mm</b> ઓન કરો.</td>
                </tr>
                <tr>
                    <td><b>૨. કાપડ ખેંચાઈ જાય છે (Fabric Puckering)</b></td>
                    <td>ડિઝાઇન બન્યા પછી કાપડમાં કરચલી પડે છે.</td>
                    <td>નીચે સપોર્ટ અંડરલે (Underlay) નથી આપ્યો અથવા કાપડ પાતળું હોવા છતાં પુલ કોમ્પનસેશન નથી.</td>
                    <td><b>Underlay Tool</b> ઓન કરો અને <b>Pull Compensation = 0.20 mm થી 0.30 mm</b> સેટ કરો.</td>
                </tr>
                <tr>
                    <td><b>૩. કાચની નળી ભાંગી જાય છે (Needle hits Cutdana)</b></td>
                    <td>સોય તૂટે છે અને કાચના કટદાણા ફૂટી જાય છે.</td>
                    <td>૪ mm નળી માટે ટાંકો ૪ mm જ રાખ્યો છે, જેથી સોય કાચના મોં પર અથડાય છે.</td>
                    <td>નળી કરતાં 0.5 mm મોટો ટાંકો આપો: <b>Taka = 4.50 mm</b> કરો અને ખૂણા પર <b>Alt+Y Cut</b> આપો.</td>
                </tr>
                <tr>
                    <td><b>૪. ટિકી ઊખડી જાય છે (Sequin Falling Off)</b></td>
                    <td>કાપડ ધોવાયા કે ઇસ્ત્રી કર્યા પછી ટિકી નીકળી જાય છે.</td>
                    <td>સિક્વિન માટે સાદો રન ટાંકો વપરાયો છે અથવા Tie-off લોક નથી.</td>
                    <td>સિક્વિન સેટિંગમાં <b>Fix Type 26 (ત્રિકોણ લોક)</b> પસંદ કરો અને અંતે ૩ ટાંકા ટાઇ લોક આપો.</td>
                </tr>
                <tr>
                    <td><b>૫. ડિઝાઇનની લંબાઈ ઘટી જાય છે (Shrinkage)</b></td>
                    <td>૧૦૦ mm ની બોર્ડર કાપડ પર ૯૫ mm ની જ બને છે.</td>
                    <td>ટાંકાના ખેંચાણ (Drag Factor) ની ગણતરી નથી કરી.</td>
                    <td>EmCAD માં સ્કેલ <b>102% થી 103%</b> મોટો કરો (Ctrl+S) જેથી મશીન પર ખેંચાઈને પરફેક્ટ ૧૦૦ mm બને.</td>
                </tr>
                <tr>
                    <td><b>૬. સોય ફ્રેમ સાથે અથડાય છે (Frame Crash)</b></td>
                    <td>મોટો ધડાકો થાય છે અને સોય-ફ્રેમ તૂટે છે.</td>
                    <td>ઓરિજિન પોઇન્ટ લોક નથી કર્યો અને ડિઝાઇન ૪૦૦ mm એરિયાથી બહાર ગઈ છે.</td>
                    <td>હંમેશા <b>Ctrl + Home</b> આપી <b>DR 250 (X=0, Y=0)</b> લોક કરો અને 5 mm સેફ્ટી માર્જિન રાખો.</td>
                </tr>
                <tr>
                    <td><b>૭. છેડા પર ગૂંચવાડો (Birdnesting)</b></td>
                    <td>ઓબ્જેક્ટના છેડા પર નીચે દોરાનો મોટો ઢગલો બને છે.</td>
                    <td>Auto-Trim પછી ટેન્શન લૂઝ રહે છે અથવા End Lock સ્ટીચ નથી.</td>
                    <td>Object Property -> Connectors માં <b>Automatic End Lock (Tie-Off)</b> એક્ટિવ કરો.</td>
                </tr>
                <tr>
                    <td><b>૮. કલર બદલતી વખતે દોરો છૂટી જવો</b></td>
                    <td>સોય બદલાયા પછી પહેલો ટાંકો પકડાતો નથી.</td>
                    <td>Color Change પછી Start Tie-in લોક નથી મૂક્યો.</td>
                    <td>Needle Change કમાન્ડ પછી તરત ૩ નાના ટાંકા આગળ-પાછળ ચલાવતો <b>Start Lock</b> મૂકો.</td>
                </tr>
                <tr>
                    <td><b>૯. સાડી પલ્લુ અસમાન રહેવું</b></td>
                    <td>ડાબી બાજુનો બુટ્ટો અને જમણી બાજુનો બુટ્ટો મળતા નથી.</td>
                    <td>પલ્લુ મિરર ૫૬૦ mm સેન્ટર લાઇન પર લોક નથી કર્યો.</td>
                    <td><b>Step 15 નિયમ:</b> ૪૦૦ mm એરિયામાં બરાબર ૧૬૦ mm / ૫૬૦ mm સેન્ટર ગાઇડલાઇન પર 'R' થી મિરર કરો.</td>
                </tr>
                <tr>
                    <td><b>૧૦. દહાઓ મશીન ફાઇલ વાંચતું નથી</b></td>
                    <td>પેનડ્રાઇવ મશીનમાં નાખતા 'File Error' આવે છે.</td>
                    <td>.DHP માસ્ટર ફાઇલ સીધી પેનડ્રાઇવમાં નાખી છે જે મશીન સપોર્ટ કરતું નથી.</td>
                    <td>Export માં જઈ <b>.DST (Tajima)</b> અથવા <b>.DHE (Dahao Beads)</b> ફોર્મેટમાં ફાઇલ સેવ કરો.</td>
                </tr>
            </tbody>
        </table>
    </div>
    """


    sec_projects = """
    <div class="section-card" id="sec-projects">
        <div class="section-header">
            <div class="section-title">
                <span>🎯</span> Section 17B: 3 Real-World Hands-on Punching Projects
            </div>
            <span class="section-tag">લાઈવ પ્રેક્ટિકલ ટ્યુટોરીયલ: શરૂઆતથી અંત સુધી</span>
        </div>
        <p style="margin-bottom: 16px;">
            નવા પંચિંગ માસ્ટર બનવા માટે થિયરી પછી આ ત્રણ વાસ્તવિક પ્રોજેક્ટ્સ કમ્પ્યુટર પર જાતે બનાવવા ફરજિયાત છે:
        </p>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 20px;">
            <!-- PROJECT 1 -->
            <div class="project-step" style="border-left-color: #059669; background: #FFFFFF; padding: 18px; border-radius: 8px; box-shadow: var(--shadow);">
                <h4 style="color: #059669; font-size: 16px; margin-bottom: 8px;">🌸 પ્રોજેક્ટ ૧: સાદી ફ્લાવર બુટ્ટી (50mm x 50mm)</h4>
                <p style="font-size: 12.5px; color: #64748B; margin-bottom: 12px;">સૌથી સરળ વેલ-બુટ્ટી જે કુરતી અને સાડીમાં વપરાય છે.</p>
                <ol style="padding-left: 18px; font-size: 12.5px; line-height: 1.6; color: #334155;">
                    <li><b>સ્કેચ ઇમ્પોર્ટ:</b> સ્કેન કરેલો ફોટો EmCAD માં લાવો અને 50 mm સાઇઝ સેટ કરો.</li>
                    <li><b>પાઘડી પાંદડી (F4):</b> F4 દબાવો -> 1100 Enter આપો -> ડાબે 'D' ખૂણો, વચ્ચે 'O' વળાંક અને જમણે 'D' ખૂણો આપી એન્ટર કરો.</li>
                    <li><b>ડાળી (F8 Run):</b> F8 દબાવી 2.5 mm સ્ટીચ લંબાઈ સાથે વળાંકવાળી ડાળી દોરો.</li>
                    <li><b>મિરરિંગ ('R'):</b> પાંદડી સિલેક્ટ કરી 'R' દબાવો અને સેન્ટર લાઇન પર બે ક્લિક આપી બીજી બાજુ નકલ બનાવો.</li>
                    <li><b>સેવ & લોક:</b> Ctrl + Home આપી DR 250 લોક કરો અને <code>Butti_01.DST</code> સેવ કરો.</li>
                </ol>
            </div>

            <!-- PROJECT 2 -->
            <div class="project-step" style="border-left-color: #1E6091; background: #FFFFFF; padding: 18px; border-radius: 8px; box-shadow: var(--shadow);">
                <h4 style="color: #1E6091; font-size: 16px; margin-bottom: 8px;">📐 પ્રોજેક્ટ ૨: સાડીની લેસ બોર્ડર (300mm Standard Lace)</h4>
                <p style="font-size: 12.5px; color: #64748B; margin-bottom: 12px;">સુરત ટેક્સટાઇલ માર્કેટની સ્ટાન્ડર્ડ 300 mm હાફ-ડ્રોપ બોર્ડર.</p>
                <ol style="padding-left: 18px; font-size: 12.5px; line-height: 1.6; color: #334155;">
                    <li><b>ફાર્મા સેટિંગ:</b> 300 mm પહોળાઈ અને 150 mm ઊંચાઈની ગાઇડલાઇન મૂકો.</li>
                    <li><b>મોટીફ લેસ (F10):</b> મોટીફ સિલેક્ટ કરી <b>Seg = 3.0 mm</b> અંતર રાખી કાંગરા દોરો.</li>
                    <li><b>સપોર્ટ રન લાઇન:</b> કાંગરાની નીચે બંને બાજુ 2.0 mm અંતરે ડબલ સપોર્ટ રન સ્ટીચ ચલાવો.</li>
                    <li><b>હાફ-ડ્રોપ કોપી:</b> બોર્ડર સિલેક્ટ કરી <code>Alt + Right Arrow</code> વડે 150 mm શિફ્ટ સાથે રીપીટ ગોઠવો.</li>
                    <li><b>ચેકલિસ્ટ:</b> રીપીટ જોડાણ પર ટાંકો ઓવરલેપ ન થાય તેનું ધ્યાન રાખી <code>Lace_300mm.DST</code> એક્સપોર્ટ કરો.</li>
                </ol>
            </div>

            <!-- PROJECT 3 -->
            <div class="project-step" style="border-left-color: #D97706; background: #FFFFFF; padding: 18px; border-radius: 8px; box-shadow: var(--shadow);">
                <h4 style="color: #D97706; font-size: 16px; margin-bottom: 8px;">👑 પ્રોજેક્ટ ૩: લગ્ન-પોશાક ગળું (Bridal Neckline Work)</h4>
                <p style="font-size: 12.5px; color: #64748B; margin-bottom: 12px;">સિક્વિન, કટદાણા અને 3D દોરી વાળું હેવી બ્રાઇડલ ગળું.</p>
                <ol style="padding-left: 18px; font-size: 12.5px; line-height: 1.6; color: #334155;">
                    <li><b>નેકલાઇન આકાર:</b> બેઝિયર કર્વ વડે ગળાનો ગોળ કે પાન આકાર દોરો.</li>
                    <li><b>3D દોરી (F12):</b> ગળાની મુખ્ય કિનારી પર F12 કોર્ડિંગ મૂકો (Angle 50, 35, 21; Times 2).</li>
                    <li><b>સિક્વિન ભરાવ:</b> ગળાની અંદરની પટ્ટીમાં Sequin -> <b>Fix Type 26 (ત્રિકોણ લોક)</b> થી Overlap Sew ભરો.</li>
                    <li><b>કટદાણા બોર્ડર:</b> બહારની લાઇન પર Beads B (4mm નળી) સેટ કરો (Taka = 4.50 mm, Alt+CapsLock 9°).</li>
                    <li><b>Fix Adjust:</b> <code>Ctrl + A -> Fix Adjust</code> કરી ડબલ કાણાં સાફ કરો અને DR 250 ઓરિજિન લોક કરો.</li>
                </ol>
            </div>
        </div>
    </div>
    """


    sec_roadmap = """
    <div class="section-card" id="sec-roadmap">
        <div class="section-header">
            <div class="section-title">
                <span>🗓️</span> Section 17C: 7-Day Step-by-Step Learning Roadmap
            </div>
            <span class="section-tag">ઝીરોથી પંચિંગ માસ્ટર બનવાનો ૭ દિવસનો પ્લાન</span>
        </div>
        <p style="margin-bottom: 16px;">
            જો કોઈ નવો વિદ્યાર્થી દરરોજ ૨ થી ૩ કલાક નીચે મુજબ પ્રેક્ટિસ કરે, તો માત્ર ૭ દિવસમાં સંપૂર્ણ પ્રોફેશનલ પંચિંગ માસ્ટર બની શકે છે:
        </p>

        <div style="display: flex; flex-direction: column; gap: 14px;">
            <div style="background: #FFFFFF; border-left: 4px solid #1E6091; padding: 14px 18px; border-radius: 6px; box-shadow: var(--shadow);">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
                    <b style="color: #0F294A; font-size: 14px;">📅 દિવસ ૧: સોફ્ટવેર પરિચય, બેઝિક શેપ્સ & શોર્ટકટ્સ</b>
                    <span class="badge-code">Tools 01-15 | Step 1 & 2</span>
                </div>
                <p style="font-size: 12.5px; color: #475569; margin: 0;">Select Tool, H (Shape Edit), B (Break), J (Weld), 'R' (Mirror), A-B-C-D આકારો અને સર્કલ રન ફ્લાવર બનાવતા શીખવું.</p>
            </div>

            <div style="background: #FFFFFF; border-left: 4px solid #059669; padding: 14px 18px; border-radius: 6px; box-shadow: var(--shadow);">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
                    <b style="color: #0F294A; font-size: 14px;">📅 દિવસ ૨: પાઘડી માસ્ટરી (F4 Column vs F2 Satin)</b>
                    <span class="badge-code">Step 3 | F4 vs F2</span>
                </div>
                <p style="font-size: 12.5px; color: #475569; margin: 0;">કોલમ સિમેટ્રી (F4), પહોળાઈ 1100 -> Enter, Node 'D' (ચોરસ ખૂણો) અને 'O' (ગોળ વળાંક) વડે કેરી અને પાંદડીઓ પંચ કરવી.</p>
            </div>

            <div style="background: #FFFFFF; border-left: 4px solid #D97706; padding: 14px 18px; border-radius: 6px; box-shadow: var(--shadow);">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
                    <b style="color: #0F294A; font-size: 14px;">📅 દિવસ ૩: તમામ સ્ટીચ પ્રકારો (F1 થી F12 ફંક્શન કીઝ)</b>
                    <span class="badge-code">Step 5 | F1 to F12</span>
                </div>
                <p style="font-size: 12.5px; color: #475569; margin: 0;">F3 તતામી ફીલ (3x Enter), F6 પેરેલલ, F8 સિંગલ રન, F9 ટ્રીપલ રન, F10 મોટીફ રન અને F12 કોર્ડિંગ સેટિંગ્સની પ્રેક્ટિસ.</p>
            </div>

            <div style="background: #FFFFFF; border-left: 4px solid #8B5CF6; padding: 14px 18px; border-radius: 6px; box-shadow: var(--shadow);">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
                    <b style="color: #0F294A; font-size: 14px;">📅 દિવસ ૪: મશીન રીપીટ, ફાર્મા સેટઅપ અને સાડી પંચિંગ</b>
                    <span class="badge-code">Step 6, 12, 15</span>
                </div>
                <p style="font-size: 12.5px; color: #475569; margin: 0;">300mm / 400mm ફાર્મા, સેન્ટર ક્રોસલાઇન X=0 Y=0, ૨૫-હેડ મશીન શિફ્ટ અને પલ્લુ મિરર ૫૬૦ mm સેન્ટર લોક પદ્ધતિ.</p>
            </div>

            <div style="background: #FFFFFF; border-left: 4px solid #EC4899; padding: 14px 18px; border-radius: 6px; box-shadow: var(--shadow);">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
                    <b style="color: #0F294A; font-size: 14px;">📅 દિવસ ૫: સિક્વિન (ટિકી) અને બીડ્સ (મોતી/કટદાણા) ડિવાઇસ</b>
                    <span class="badge-code">Step 11 & 16</span>
                </div>
                <p style="font-size: 12.5px; color: #475569; margin: 0;">Fix Type 26 ત્રિકોણ લોક, Overlap Sew, ગોળ મોતી ટાંકો 2.30mm, કટદાણા 4.50mm, Alt+CapsLock ૯° અને Fix Adjust.</p>
            </div>

            <div style="background: #FFFFFF; border-left: 4px solid #06B6D4; padding: 14px 18px; border-radius: 6px; box-shadow: var(--shadow);">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
                    <b style="color: #0F294A; font-size: 14px;">📅 દિવસ ૬: ૯-સોય શેડિંગ ફ્લાવર, ફ્લોરેન્ટાઇન & 3D દોરી</b>
                    <span class="badge-code">Step 9 | Color Shading</span>
                </div>
                <p style="font-size: 12.5px; color: #475569; margin: 0;">1 થી 6 કલર કીઝ, ૯૦° પરપેન્ડીક્યુલર તતામી ફીલ, વળાંકવાળી ફ્લોરેન્ટાઇન એંગલ લાઇન્સ અને આઇલેન્ડ કોર્ડિંગ પદ્ધતિ.</p>
            </div>

            <div style="background: #FFFFFF; border-left: 4px solid #10B981; padding: 14px 18px; border-radius: 6px; box-shadow: var(--shadow);">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
                    <b style="color: #0F294A; font-size: 14px;">📅 દિવસ ૭: ફાઇનલ પ્રોડક્શન ચેકલિસ્ટ, DR 250 લોક & એક્સપોર્ટ</b>
                    <span class="badge-code">Step 13, 14, 16</span>
                </div>
                <p style="font-size: 12.5px; color: #475569; margin: 0;">Start/End Lock, Jump Control, Ctrl+Home આપી DR 250 ઓરિજિન લોક, .DHP બેકઅપ અને .DST/.DHE મશીન પેનડ્રાઇવ એક્સપોર્ટ.</p>
            </div>
        </div>
    </div>
    """


    sec_slang = """
    <div class="section-card" id="sec-slang">
        <div class="section-header">
            <div class="section-title">
                <span>📖</span> Section 17D: Surat Textile Market Slang Dictionary
            </div>
            <span class="section-tag">સુરત ફેક્ટરી અને ખાતાની દેશી ભાષા શબ્દકોશ</span>
        </div>
        <p style="margin-bottom: 16px;">
            જ્યારે તમે સુરતના કોઈપણ એમ્બ્રોઇડરી ખાતા (ફેક્ટરી) માં કામ કરવા જશો ત્યારે કારીગરો અને શેઠ નીચે મુજબના દેશી શબ્દો વાપરશે:
        </p>

        <table class="data-table">
            <thead>
                <tr>
                    <th style="width: 140px;">દેશી શબ્દ (Market Slang)</th>
                    <th style="width: 180px;">EmCAD / ટેકનિકલ ટર્મ</th>
                    <th>ફેક્ટરી અર્થ અને પ્રેક્ટિકલ ઉપયોગ</th>
                </tr>
            </thead>
            <tbody>
                <tr><td><b>પાઘડી</b></td><td>Satin Column Symmetry (F4)</td><td>સાટિન ટાંકાની બંને બાજુ સપ્રમાણ પહોળાઈ વાળી પાંદડી કે વેલ.</td></tr>
                <tr><td><b>તતામી / ભરાવ</b></td><td>Complex Fill / Tatami (F3)</td><td>મોટા એરિયામાં સાદડી જેવો ગૂંથેલો સપાટ ટાંકો ભરવો.</td></tr>
                <tr><td><b>તળિયું</b></td><td>Foundation Underlay</td><td>મુખ્ય ટાંકા નીચે કાપડને પકડવા માટે અગાઉથી મરાતો હળવો સપોર્ટ ટાંકો.</td></tr>
                <tr><td><b>ટાંકો</b></td><td>Stitch Length (mm)</td><td>સોયના બે પંચ વચ્ચેનું અંતર (દા.ત. 2.5 mm રન ટાંકો).</td></tr>
                <tr><td><b>કાંગરી</b></td><td>E-Stitch / Border Kangri</td><td>એક બાજુ સીધી અને બીજી બાજુ કાંટાવાળી બોર્ડર સ્ટીચ.</td></tr>
                <tr><td><b>નળી / પાઇપ</b></td><td>Cutdana Bugle Beads (Beads B)</td><td>૪ mm લાંબી હેક્સાગોનલ કાચની ચમકતી પાઇપ.</td></tr>
                <tr><td><b>ટિકી</b></td><td>Metallic Sequin Disc</td><td>ગોળ ચમકતી પતરી જે મશીન ફીડર વડે ડ્રોપ થાય છે.</td></tr>
                <tr><td><b>દોરી વર્ક</b></td><td>Cording / Dori (F12)</td><td>કાપડ પર જાડી સોનેરી જરીની દોરી ઝિગઝેગ ટાંકા વડે ટાંકવી.</td></tr>
                <tr><td><b>ફાર્મા</b></td><td>Repeat Frame Size</td><td>ડિઝાઇનની એક રીપીટની ફ્રેમ સાઇઝ (દા.ત. 300 mm / 400 mm).</td></tr>
                <tr><td><b>ઝીરો / ઓરિજિન</b></td><td>Machine Origin Point (0,0)</td><td>મશીનનું મૂળ શરૂઆતનું સ્થાન (DR 250 / Ctrl+Home).</td></tr>
                <tr><td><b>પલ્લું મિરર</b></td><td>Saree Pally Mirror ('R')</td><td>સાડીના પાલવમાં બંને બાજુ સામસામે એકસરખો બુટ્ટો બેસાડવો.</td></tr>
                <tr><td><b>ખાટલી વર્ક</b></td><td>Hand-look Beads Embroidery</td><td>હાથેથી સોય-દોરાથી કરેલું હોય તેવું લક્ઝરી મોતી-કટદાણા વર્ક.</td></tr>
                <tr><td><b>ખાતો</b></td><td>Embroidery Factory / Unit</td><td>સુરતમાં જ્યાં ૨૫-હેડ વાળા મશીનો ચાલતા હોય તે એમ્બ્રોઇડરી કારખાનું.</td></tr>
                <tr><td><b>ટાંકા ખેંચાવવા</b></td><td>Fabric Puckering</td><td>કાપડ ખેંચાઈને કરચલી પડવી (અંડરલેના અભાવે).</td></tr>
                <tr><td><b>ચોરસ / ગોળ નોડ</b></td><td>Node 'D' (Square) & Node 'O' (Arc)</td><td>'D' થી ખૂણો બને અને 'O' થી સ્મૂથ ગોળ વળાંક બને.</td></tr>
            </tbody>
        </table>
    </div>
    """


    sec_dos_donts = """
    <div class="section-card" id="sec-dos-donts">
        <div class="section-header">
            <div class="section-title">
                <span>⚖️</span> Section 17E: Professional Do's & Don'ts (સારી vs ખરાબ પંચિંગ પદ્ધતિ)
            </div>
            <span class="section-tag">શું કરવું અને શું ન કરવું - સુવર્ણ નિયમો</span>
        </div>
        <p style="margin-bottom: 16px;">
            એક સાધારણ પંચર અને માસ્ટર પંચર વચ્ચેનો તફાવત આ નિયમો નક્કી કરે છે:
        </p>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 20px;">
            <!-- DONT'S -->
            <div style="background: #FEF2F2; border: 2px solid #FCA5A5; border-radius: 10px; padding: 20px;">
                <h4 style="color: #DC2626; font-size: 16px; margin-bottom: 12px; display: flex; align-items: center; gap: 8px;">
                    <span>❌</span> ક્યારેય ન કરવું (Strictly DON'T)
                </h4>
                <ul style="padding-left: 18px; font-size: 13px; line-height: 1.6; color: #7F1D1D;">
                    <li><b>તીક્ષ્ણ વળાંક પર શોર્ટ સ્ટીચ બંધ ન રાખો:</b> નહીંતર અંદરની બાજુ ટાંકા ગૂંચવાઈને સોય તૂટશે.</li>
                    <li><b>ઓપન જમ્પ ખુલ્લા ન છોડો:</b> સાટિન કે તતામી નીચે ટ્રાવેલ રન સ્ટીચ છુપાવો જેથી દોરો ન દેખાય.</li>
                    <li><b>સિક્વિનમાં સાદો ટાંકો ન વાપરો:</b> હંમેશા Fix Type 26 ત્રિકોણ લોક જ વાપરો.</li>
                    <li><b>કટદાણા માટે નાનો ટાંકો ન રાખો:</b> ૪ mm નળી માટે ૪ mm ટાંકો રાખશો તો સોય કાચ સાથે અથડાશે.</li>
                    <li><b>ઓરિજિન લોક (DR 250) ભૂલશો નહીં:</b> ઓરિજિન વગર ૨૫-હેડ મશીન પર ફ્રેમ હિટ થઈ શકે છે.</li>
                </ul>
            </div>

            <!-- DO'S -->
            <div style="background: #ECFDF5; border: 2px solid #6EE7B7; border-radius: 10px; padding: 20px;">
                <h4 style="color: #059669; font-size: 16px; margin-bottom: 12px; display: flex; align-items: center; gap: 8px;">
                    <span>✅</span> હંમેશા કરવું (Strictly DO)
                </h4>
                <ul style="padding-left: 18px; font-size: 13px; line-height: 1.6; color: #064E3B;">
                    <li><b>Short Stitches = 0.5 mm ઓન રાખો:</b> ખૂણા અને પાઘડીના વળાંકો આપોઆપ ક્લીન થશે.</li>
                    <li><b>Start Lock (Tie-in) અને End Lock (Tie-off) આપો:</b> જેથી કાપડ ધોવાયા પછી દોરો ન છૂટે.</li>
                    <li><b>પાતળા કાપડ પર Pull Comp = 0.25 mm આપો:</b> જેથી કાપડ ખેંચાઈને કરચલી ન પડે.</li>
                    <li><b>કટદાણા નળી માટે Taka = 4.50 mm સેટ કરો:</b> નળી કરતાં હંમેશા 0.5 mm મોટો ટાંકો.</li>
                    <li><b>પંચિંગ પત્યા પછી Ctrl + A -> Fix Adjust કરો:</b> તમામ ઓવરલેપિંગ કાણાં આપોઆપ ક્લીન થશે.</li>
                </ul>
            </div>
        </div>
    </div>
    """


    sec_quiz = """
    <div class="section-card" id="sec-quiz">
        <div class="section-header">
            <div class="section-title">
                <span>🧠</span> Section 17F: Interactive EmCAD Certification Quiz (૧૦ પ્રશ્નોની ઓનલાઇન ટેસ્ટ)
            </div>
            <span class="section-tag">તમારી જાતે ચકાસણી કરો - ઇન્સ્ટન્ટ સ્કોર</span>
        </div>
        <p style="margin-bottom: 16px;">
            આ ગાઇડમાંથી તમે કેટલું શીખ્યા તે ચકાસવા માટે નીચેના પ્રશ્નોના જવાબો આપો. સાચો જવાબ આપતા તરત લીલો રંગ અને વિગતવાર ખુલાસો જોવા મળશે:
        </p>

        <div id="quizContainer">
            <!-- Q1 -->
            <div class="quiz-card" data-correct="1">
                <div class="quiz-q">પ્રશ્ન ૧: EmCAD માં બંને બાજુ સરખો વળાંક ધરાવતી પાઘડી (Column Symmetry) દોરવા કઈ ફંક્શન કી વપરાય છે?</div>
                <div class="quiz-options">
                    <div class="quiz-option" onclick="checkAnswer(this, 0)">A) F2 Simple Satin</div>
                    <div class="quiz-option" onclick="checkAnswer(this, 1)">B) F4 Column Symmetry</div>
                    <div class="quiz-option" onclick="checkAnswer(this, 2)">C) F3 Tatami Complex Fill</div>
                    <div class="quiz-option" onclick="checkAnswer(this, 3)">D) F8 Run Stitch</div>
                </div>
                <div class="quiz-feedback"></div>
            </div>

            <!-- Q2 -->
            <div class="quiz-card" data-correct="2">
                <div class="quiz-q">પ્રશ્ન ૨: ૪ mm લાંબી કાચની નળી (Cutdana Bugle Beads) માટે મશીન ટાંકો (Taka) કેટલો રાખવો જોઈએ?</div>
                <div class="quiz-options">
                    <div class="quiz-option" onclick="checkAnswer(this, 0)">A) 2.15 mm</div>
                    <div class="quiz-option" onclick="checkAnswer(this, 1)">B) 3.50 mm</div>
                    <div class="quiz-option" onclick="checkAnswer(this, 2)">C) 4.50 mm (નળી કરતાં 0.5 mm વધુ)</div>
                    <div class="quiz-option" onclick="checkAnswer(this, 3)">D) 6.00 mm</div>
                </div>
                <div class="quiz-feedback"></div>
            </div>

            <!-- Q3 -->
            <div class="quiz-card" data-correct="1">
                <div class="quiz-q">પ્રશ્ન ૩: ગોળ સિક્વિન (ટિકી) ધોવાયા પછી ઊખડી ન જાય તે માટે કયો લોક ટાંકો (Fix Type) સૌથી શ્રેષ્ઠ છે?</div>
                <div class="quiz-options">
                    <div class="quiz-option" onclick="checkAnswer(this, 0)">A) Fix Type 01 (સિંગલ ટાંકો)</div>
                    <div class="quiz-option" onclick="checkAnswer(this, 1)">B) Fix Type 26 (૩-પોઇન્ટ ત્રિકોણ લોક / 120° Tie)</div>
                    <div class="quiz-option" onclick="checkAnswer(this, 2)">C) Cross Stitch</div>
                    <div class="quiz-option" onclick="checkAnswer(this, 3)">D) E-Stitch</div>
                </div>
                <div class="quiz-feedback"></div>
            </div>

            <!-- Q4 -->
            <div class="quiz-card" data-correct="0">
                <div class="quiz-q">પ્રશ્ન ૪: ડિઝાઇન સિલેક્ટ કરી કીબોર્ડ પરથી 'R' દબાવી સેન્ટરમાં બે ક્લિક આપવાથી કયું કાર્ય થાય છે?</div>
                <div class="quiz-options">
                    <div class="quiz-option" onclick="checkAnswer(this, 0)">A) મિરરિંગ (Mirror - આડી કે ઊભી અરીસા જેવી નકલ)</div>
                    <div class="quiz-option" onclick="checkAnswer(this, 1)">B) રોટેટ (Rotate 90°)</div>
                    <div class="quiz-option" onclick="checkAnswer(this, 2)">C) ઓબ્જેક્ટ ડિલીટ</div>
                    <div class="quiz-option" onclick="checkAnswer(this, 3)">D) સ્ટીચિંગ શરૂ</div>
                </div>
                <div class="quiz-feedback"></div>
            </div>

            <!-- Q5 -->
            <div class="quiz-card" data-correct="2">
                <div class="quiz-q">પ્રશ્ન ૫: બીડ્સ કે સિક્વિનને ૯ ડિગ્રી ના એંગલ પર ફેરવવા માટે કઈ શોર્ટકટ કી વપરાય છે?</div>
                <div class="quiz-options">
                    <div class="quiz-option" onclick="checkAnswer(this, 0)">A) Ctrl + R</div>
                    <div class="quiz-option" onclick="checkAnswer(this, 1)">B) Shift + Rotate</div>
                    <div class="quiz-option" onclick="checkAnswer(this, 2)">C) Alt + CapsLock</div>
                    <div class="quiz-option" onclick="checkAnswer(this, 3)">D) Alt + Shift + V</div>
                </div>
                <div class="quiz-feedback"></div>
            </div>

            <!-- Q6 -->
            <div class="quiz-card" data-correct="1">
                <div class="quiz-q">પ્રશ્ન ૬: F2 સાટિન ઓબ્જેક્ટને સીધું F3 તતામી ફીલમાં કન્વર્ટ કરવા માટે કઈ ટ્રીક વપરાય છે?</div>
                <div class="quiz-options">
                    <div class="quiz-option" onclick="checkAnswer(this, 0)">A) Ctrl + F3</div>
                    <div class="quiz-option" onclick="checkAnswer(this, 1)">B) F3 દબાવી ૩ વખત Enter આપવું</div>
                    <div class="quiz-option" onclick="checkAnswer(this, 2)">C) Delete કરી ફરી દોરવું</div>
                    <div class="quiz-option" onclick="checkAnswer(this, 3)">D) Alt + T</div>
                </div>
                <div class="quiz-feedback"></div>
            </div>

            <!-- Q7 -->
            <div class="quiz-card" data-correct="3">
                <div class="quiz-q">પ્રશ્ન ૭: F12 કોર્ડિંગ (દોરી વર્ક) માટે સ્ટાન્ડર્ડ એંગલ અને ટાઈમ્સ સેટિંગ કયા છે?</div>
                <div class="quiz-options">
                    <div class="quiz-option" onclick="checkAnswer(this, 0)">A) Angle = 10, 20; Times = 1</div>
                    <div class="quiz-option" onclick="checkAnswer(this, 1)">B) Angle = 90; Times = 4</div>
                    <div class="quiz-option" onclick="checkAnswer(this, 2)">C) Angle = 45; Times = 3</div>
                    <div class="quiz-option" onclick="checkAnswer(this, 3)">D) Angle = 50, 35, 21; Times = 2</div>
                </div>
                <div class="quiz-feedback"></div>
            </div>

            <!-- Q8 -->
            <div class="quiz-card" data-correct="0">
                <div class="quiz-q">પ્રશ્ન ૮: ૨૫-હેડ મશીન પર ફ્રેમ હિટ (Crash) અટકાવવા ડિઝાઇન પૂરી થયા પછી કયો ઓરિજિન લોક કરવો ફરજિયાત છે?</div>
                <div class="quiz-options">
                    <div class="quiz-option" onclick="checkAnswer(this, 0)">A) Ctrl + Home આપી DR 250 (X=0, Y=0)</div>
                    <div class="quiz-option" onclick="checkAnswer(this, 1)">B) Shift + F1</div>
                    <div class="quiz-option" onclick="checkAnswer(this, 2)">C) Alt + End</div>
                    <div class="quiz-option" onclick="checkAnswer(this, 3)">D) ESC Lock</div>
                </div>
                <div class="quiz-feedback"></div>
            </div>

            <!-- Q9 -->
            <div class="quiz-card" data-correct="2">
                <div class="quiz-q">પ્રશ્ન ૯: પંચિંગમાં 'D' અને 'O' કીઝનો શો ઉપયોગ થાય છે?</div>
                <div class="quiz-options">
                    <div class="quiz-option" onclick="checkAnswer(this, 0)">A) Delete અને Open</div>
                    <div class="quiz-option" onclick="checkAnswer(this, 1)">B) Density અને Outline</div>
                    <div class="quiz-option" onclick="checkAnswer(this, 2)">C) 'D' = તીક્ષ્ણ ચોરસ ખૂણો (Corner) અને 'O' = સ્મૂથ ગોળ વળાંક (Curve Arc)</div>
                    <div class="quiz-option" onclick="checkAnswer(this, 3)">D) Dark અને Output</div>
                </div>
                <div class="quiz-feedback"></div>
            </div>

            <!-- Q10 -->
            <div class="quiz-card" data-correct="1">
                <div class="quiz-q">પ્રશ્ન ૧૦: પંચિંગ પૂર્ણ થયા પછી ઓવરલેપિંગ કાણાં અને ડબલ બીડ્સ સાફ કરવા કયો કમાન્ડ આપવો જોઈએ?</div>
                <div class="quiz-options">
                    <div class="quiz-option" onclick="checkAnswer(this, 0)">A) Format Drive</div>
                    <div class="quiz-option" onclick="checkAnswer(this, 1)">B) Ctrl + A -> Stitch -> Fix Adjust</div>
                    <div class="quiz-option" onclick="checkAnswer(this, 2)">C) Shift + Delete</div>
                    <div class="quiz-option" onclick="checkAnswer(this, 3)">D) Auto Trim All</div>
                </div>
                <div class="quiz-feedback"></div>
            </div>
        </div>

        <div id="quizScoreBox" style="display:none; background:#0F294A; color:#fff; padding:20px; border-radius:10px; text-align:center; margin-top:20px;">
            <h3 style="color:#F59E0B; margin-bottom:8px;">🏆 ક્વિઝ પરિણામ: <span id="quizScore">0</span> / ૧૦</h3>
            <p id="quizScoreMsg" style="font-size:14px; color:#E2E8F0;"></p>
        </div>
    </div>
    """

    sec17 = """
    <div class="section-card" id="sec-shortcuts">
        <div class="section-header">
            <div class="section-title">
                <span>⚡</span> Section 17: Master Shortcut Cheat Sheet & Operator's Golden Rules
            </div>
            <span class="section-tag">તમામ શોર્ટકટ્સની યાદી અને ચેકલિસ્ટ</span>
        </div>
        <p style="margin-bottom: 16px;">
            પંચિંગ માસ્ટરની ઝડપ તેના કીબોર્ડ શોર્ટકટ્સ પર નિર્ભર કરે છે. માઉસનો ઓછો અને કીબોર્ડનો વધુ ઉપયોગ કરો.
        </p>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 20px;">
            <div>
                <h3 style="color: var(--primary); margin-bottom: 8px;">⌨️ પંચિંગ માસ્ટર શોર્ટકટ્સ</h3>
                <table class="data-table">
                    <thead><tr><th>શોર્ટકટ કી</th><th>કાર્ય અને પંચિંગ અસર</th></tr></thead>
                    <tbody>
                        <tr><td><span class="badge-code">Spacebar</span></td><td>Select Tool મોડમાં પાછા ફરવા.</td></tr>
                        <tr><td><span class="badge-code">H</span></td><td>Shape Edit - નોડ્સ, પોઇન્ટ્સ અને હેન્ડલ્સ સુધારવા.</td></tr>
                        <tr><td><span class="badge-code">E</span></td><td>Edit Stitch - સિંગલ ટાંકો સુધારવા કે ડીલીટ કરવા.</td></tr>
                        <tr><td><span class="badge-code">B</span></td><td>Break - લાઇન કે ઓબ્જેક્ટને વચ્ચેથી તોડવા.</td></tr>
                        <tr><td><span class="badge-code">J</span></td><td>Weld / Join - બે શેપ્સને જોડીને એક બનાવવા.</td></tr>
                        <tr><td><span class="badge-code">R</span></td><td>Mirror - બે ક્લિક આપી આડી કે ઊભી નકલ કરવી.</td></tr>
                        <tr><td><span class="badge-code">Q</span></td><td>Center Object - ઓબ્જેક્ટને બરાબર મધ્યમાં લાવવા.</td></tr>
                        <tr><td><span class="badge-code">Shift + X</span></td><td>Start અને End પોઇન્ટ અરસપરસ બદલવા.</td></tr>
                        <tr><td><span class="badge-code">Ctrl + D</span></td><td>Duplicate - ઓબ્જેક્ટની તુરંત નકલ બનાવવા.</td></tr>
                        <tr><td><span class="badge-code">Alt + Shift + V</span></td><td>Paste in Place - મૂળ જગ્યાએ જ ચોક્કસ પેસ્ટ.</td></tr>
                        <tr><td><span class="badge-code">Alt + -></span></td><td>Step Copy - ચોક્કસ અંતરે લાઇનસર કોપી.</td></tr>
                        <tr><td><span class="badge-code">Alt + CapsLock</span></td><td>Beads / Sequin ને ૯ ડિગ્રી ના એંગલે ફેરવવા.</td></tr>
                        <tr><td><span class="badge-code">Alt + Y</span></td><td>Object Cut (બીડ્સ બ્રેકડાઉન કટ).</td></tr>
                        <tr><td><span class="badge-code">Alt + B</span></td><td>Beads Split (બીડ્સ લાઇન વિભાજિત કરવી).</td></tr>
                        <tr><td><span class="badge-code">F3 + 3x Enter</span></td><td>F2 સાટિનને સીધું F3 તતામી ફીલમાં કન્વર્ટ કરવું.</td></tr>
                        <tr><td><span class="badge-code">0 (Zero)</span></td><td>Fit to Screen - આખી ડિઝાઇન સ્ક્રીન પર ફિટ કરવી.</td></tr>
                        <tr><td><span class="badge-code">Ctrl + Home</span></td><td>Set Machine Origin (X=0, Y=0 DR250).</td></tr>
                    </tbody>
                </table>
            </div>

            <div>
                <h3 style="color: var(--primary); margin-bottom: 8px;">📋 પ્રોડક્શન પહેલાંની ગોલ્ડન ચેકલિસ્ટ</h3>
                <table class="data-table">
                    <thead><tr><th>ક્રમ & વિષય</th><th>ચકાસણી મુદ્દો (Golden Checklist)</th></tr></thead>
                    <tbody>
                        <tr><td><b>૧. માપ ચકાસણી</b></td><td>ડિઝાઇન સાચી સાઇઝ (mm) માં છે? ફ્રેમ માર્જિન 5 mm જળવાયું છે?</td></tr>
                        <tr><td><b>૨. જમ્પ કંટ્રોલ</b></td><td>૫ mm થી મોટા તમામ જમ્પ પર ટ્રાવેલ રન સ્ટીચ મૂકી છે?</td></tr>
                        <tr><td><b>૩. લોક ટાંકા</b></td><td>દરેક ઓબ્જેક્ટની શરૂઆતમાં Tie-in અને છેડે Tie-off છે?</td></tr>
                        <tr><td><b>૪. શોર્ટ સ્ટીચ</b></td><td>તીક્ષ્ણ વળાંક પર Short Stitches = 0.5 mm સેટ છે?</td></tr>
                        <tr><td><b>૫. બીડ્સ ટાંકો</b></td><td>મોતીના વ્યાસ મુજબ યોગ્ય ટાંકો (2.15 થી 4.5 mm) સેટ છે?</td></tr>
                        <tr><td><b>૬. ફિક્સ એડજસ્ટ</b></td><td>Ctrl + A કરી Stitch -> Fix Adjust રન કર્યું છે?</td></tr>
                        <tr><td><b>૭. ઓરિજિન લોક</b></td><td>X=0, Y=0 (DR 250) ઓરિજિન પોઇન્ટ લોક કર્યો છે?</td></tr>
                        <tr><td><b>૮. બેકઅપ ફાઇલ</b></td><td>.DHP માસ્ટર ફાઇલ અને .DST / .DHE મશીન ફાઇલ પેનડ્રાઇવમાં સેવ કરી?</td></tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
    """
    return [sec1, sec2, sec_animations, sec_comparisons, sec3, sec4, sec5, sec6, sec7, sec8, sec9, sec10, sec11, sec12, sec12b, sec13, sec14, sec15, sec16, sec_drive_gallery, sec_troubleshooting, sec_projects, sec_roadmap, sec_slang, sec_dos_donts, sec_quiz, sec17]

def main():
    print("Building full HTML document...")
    sections = assemble_sections()
    body_content = "\n".join(sections)
    full_html = HTML_HEAD + body_content + HTML_FOOT

    with open(HTML_OUTPUT, 'w', encoding='utf-8') as f:
        f.write(full_html)
    print(f"HTML Handbook saved to: {HTML_OUTPUT} ({len(full_html)} bytes)")

    print("Compiling publication-grade PDF via Headless Chrome...")
    cmd = [
        CHROME_BIN,
        '--headless',
        '--disable-gpu',
        '--no-pdf-header-footer',
        f'--print-to-pdf={PDF_OUTPUT}',
        f'file://{HTML_OUTPUT}'
    ]
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if os.path.exists(PDF_OUTPUT):
        size_mb = os.path.getsize(PDF_OUTPUT) / (1024 * 1024)
        print(f"Master PDF compiled successfully: {PDF_OUTPUT} ({size_mb:.2f} MB)")
    else:
        print(f"Error compiling PDF: {res.stderr}")

if __name__ == '__main__':
    main()
