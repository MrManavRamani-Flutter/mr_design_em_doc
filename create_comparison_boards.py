#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EmCAD Visual Comparison Boards Builder
Creates 6 high-resolution side-by-side comparison graphics:
1. Paghdi (Column Symmetry F4): Vector Drawing vs Real Satin Stitch Design
2. Sequin (ટિકી): Vector Path & Fix Type 26 vs Real Overlapping Sequins
3. Beads (મોતી / કટદાણા): Vector Spacing & Taka Table vs Real Glass Pearls & Bugle Beads
4. Mirror ('R' Key): Vector Half & Axis vs Real Symmetrical Embroidered Garment
5. Shading Flower (Tatami Fill): Vector Angle Contours vs Real Gradient Embroidered Flower
6. Cording (F12 Dori Work): Vector Core & Zigzag Tack vs Real Raised 3D Dori Embroidery
"""

import os
import math
from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageFilter, ImageOps

WORKSPACE = '/Users/manavramani/Desktop/emCad_explain_software'
ASSET_DIR = os.path.join(WORKSPACE, 'emCad_organized_assets')
FONT_PATH = '/Library/Fonts/Arial Unicode.ttf'
BRAIN_DIR = '/Users/manavramani/.gemini/antigravity-ide/brain/a38be684-aef7-4dc9-bc56-0dce25873917'

# Real image paths generated
REAL_PAGHDI = os.path.join(BRAIN_DIR, 'real_paghdi_satin_1791611229379.jpg')
REAL_SEQUIN = os.path.join(BRAIN_DIR, 'real_sequin_embroidery_1791611249685.jpg')
REAL_BEADS = os.path.join(BRAIN_DIR, 'real_beads_pearls_1791611273744.jpg')
REAL_MIRROR = os.path.join(BRAIN_DIR, 'real_mirror_embroidery_1791611300085.jpg')
REAL_SHADED = os.path.join(BRAIN_DIR, 'real_shaded_flower_1791611322886.jpg')
REAL_CORDING = os.path.join(BRAIN_DIR, 'real_cording_dori_1791611344499.jpg')

# Colors
C_NAVY = (15, 41, 74)
C_DARK = (10, 25, 47)
C_GOLD = (217, 119, 6)
C_LIGHT_BG = (248, 250, 252)
C_WHITE = (255, 255, 255)
C_GRID = (226, 232, 240)
C_TEXT = (30, 41, 59)
C_MUTED = (100, 116, 139)
C_BLUE = (30, 96, 145)
C_GREEN = (5, 150, 105)
C_RED = (220, 38, 38)
C_MAGENTA = (192, 38, 211)

def get_font(size):
    return ImageFont.truetype(FONT_PATH, size)

def draw_vector_paghdi(w, h):
    """Draws a vector Paghdi schematic with EmCAD nodes and angle lines"""
    img = Image.new('RGB', (w, h), (250, 252, 255))
    draw = ImageDraw.Draw(img)
    
    # Draw CAD grid
    for x in range(0, w, 40):
        draw.line([(x, 0), (x, h)], fill=(235, 240, 248), width=1)
    for y in range(0, h, 40):
        draw.line([(y, 0), (y, h)], fill=(235, 240, 248), width=1)
        
    font_s = get_font(20)
    font_xs = get_font(16)
    
    # Outer column symmetry curves
    cx, cy = w // 2, h // 2
    # Draw centerline
    draw.line([(cx, 80), (cx, h - 80)], fill=(180, 195, 215), width=2)
    draw.text((cx + 10, 90), "Centerline Axis (X=0)", font=font_xs, fill=C_MUTED)
    
    # Paghdi shape outline pairs (Column Symmetry F4)
    # Left curve and Right curve
    left_pts = []
    right_pts = []
    angles = []
    
    for t in range(0, 180, 8):
        rad = math.radians(t)
        # width varies along height
        curve_y = 120 + t * 4
        half_w = 70 + 60 * math.sin(rad)
        lx = cx - half_w
        rx = cx + half_w
        left_pts.append((lx, curve_y))
        right_pts.append((rx, curve_y))
        angles.append(((lx, curve_y), (rx, curve_y)))

    # Draw satin stitch fill lines (angle lines)
    for (p1, p2) in angles[::2]:
        draw.line([p1, p2], fill=(220, 180, 100), width=3)
        
    # Draw left & right boundary
    draw.line(left_pts, fill=C_BLUE, width=4)
    draw.line(right_pts, fill=C_BLUE, width=4)
    
    # Draw EmCAD Nodes (Square 'D' for corners, Circle 'O' for curves)
    for i, pt in enumerate(left_pts[::3]):
        if i in [0, len(left_pts)//6]:
            # Square node 'D'
            draw.rectangle([(pt[0]-7, pt[1]-7), (pt[0]+7, pt[1]+7)], fill=C_RED, outline=C_DARK, width=2)
            draw.text((pt[0]-45, pt[1]-10), "Node 'D'", font=font_xs, fill=C_RED)
        else:
            # Curve node 'O'
            draw.ellipse([(pt[0]-6, pt[1]-6), (pt[0]+6, pt[1]+6)], fill=C_GREEN, outline=C_DARK, width=2)

    for i, pt in enumerate(right_pts[::3]):
        if i in [0, len(right_pts)//6]:
            draw.rectangle([(pt[0]-7, pt[1]-7), (pt[0]+7, pt[1]+7)], fill=C_RED, outline=C_DARK, width=2)
        else:
            draw.ellipse([(pt[0]-6, pt[1]-6), (pt[0]+6, pt[1]+6)], fill=C_GREEN, outline=C_DARK, width=2)
            
    # Width annotation
    mid_idx = len(left_pts) // 2
    my = left_pts[mid_idx][1]
    lx, rx = left_pts[mid_idx][0], right_pts[mid_idx][0]
    draw.line([(lx, my - 25), (rx, my - 25)], fill=C_MAGENTA, width=2)
    draw.line([(lx, my - 35), (lx, my - 15)], fill=C_MAGENTA, width=2)
    draw.line([(rx, my - 35), (rx, my - 15)], fill=C_MAGENTA, width=2)
    draw.text((cx - 100, my - 55), "Width >= 0.8 mm (1100 -> Enter)", font=font_s, fill=C_MAGENTA)
    
    # Legend overlay
    draw.rectangle([(30, h - 140), (w - 30, h - 30)], fill=(255, 255, 255, 240), outline=C_GRID, width=2)
    draw.text((45, h - 130), "EmCAD પંચિંગ કમાન્ડ: F4 Column Symmetry | 1100 સ્ટાન્ડર્ડ પહોળાઈ", font=font_s, fill=C_NAVY)
    draw.text((45, h - 100), "• લાલ સ્ક્વેર [D] = તીક્ષ્ણ ખૂણો (Corner Node)  |  • લીલો સર્કલ (O) = સ્મૂથ વળાંક (Curve Node)", font=font_xs, fill=C_TEXT)
    draw.text((45, h - 75), "• પીળા ટાંકા = સાટિન સ્ટીચ એંગલ (Satin Angle)  |  • Short Stitches = 0.5 mm સેફ્ટી", font=font_xs, fill=C_MUTED)

    return img

def draw_vector_sequin(w, h):
    """Draws a vector Sequin schematic showing drop points, center holes, and Fix Type 26"""
    img = Image.new('RGB', (w, h), (250, 252, 255))
    draw = ImageDraw.Draw(img)
    
    for x in range(0, w, 40):
        draw.line([(x, 0), (x, h)], fill=(235, 240, 248), width=1)
    for y in range(0, h, 40):
        draw.line([(y, 0), (y, h)], fill=(235, 240, 248), width=1)
        
    font_s = get_font(20)
    font_xs = get_font(16)
    
    # S-Curve path for sequin drops
    cx, cy = w // 2, h // 2
    
    # Draw Sequin Discs overlapping (Fish scale / Overlap Sew)
    num_seq = 10
    seq_radius = 45
    pts = []
    for i in range(num_seq):
        t = i / (num_seq - 1)
        sx = 120 + t * (w - 240)
        sy = cy + 120 * math.sin(t * math.pi * 1.5)
        pts.append((sx, sy))
        
    # Draw path line
    draw.line(pts, fill=(180, 195, 215), width=2)
    
    # Draw overlapping sequin discs
    for i, (sx, sy) in enumerate(pts):
        # Disc circle
        fill_col = (255, 245, 200) if i % 2 == 0 else (240, 245, 255)
        draw.ellipse([(sx - seq_radius, sy - seq_radius), (sx + seq_radius, sy + seq_radius)], fill=fill_col, outline=C_GOLD, width=2)
        # Center puncture needle hole
        draw.ellipse([(sx - 8, sy - 8), (sx + 8, sy + 8)], fill=C_DARK, outline=C_DARK)
        
        # Draw Fix Stitch Type 26 (3-point / triangle tie stitch locking sequin)
        p1 = (sx, sy - 25)
        p2 = (sx - 20, sy + 18)
        p3 = (sx + 20, sy + 18)
        draw.line([(sx, sy), p1], fill=C_RED, width=3)
        draw.line([(sx, sy), p2], fill=C_RED, width=3)
        draw.line([(sx, sy), p3], fill=C_RED, width=3)
        # Needle puncture dots at ends
        for p in [p1, p2, p3]:
            draw.ellipse([(p[0]-3, p[1]-3), (p[0]+3, p[1]+3)], fill=C_RED)

    # Annotations
    an_x, an_y = pts[4]
    draw.line([(an_x, an_y - seq_radius), (an_x + 80, an_y - seq_radius - 40)], fill=C_BLUE, width=2)
    draw.text((an_x + 85, an_y - seq_radius - 55), "Sequin Disc (ટિકી વ્યાસ 2-5mm)", font=font_s, fill=C_BLUE)

    draw.line([(an_x, an_y), (an_x + 100, an_y + 40)], fill=C_RED, width=2)
    draw.text((an_x + 105, an_y + 30), "Fix Type 26 (ત્રિકોણ લોક ટાંકો)", font=font_s, fill=C_RED)
    
    # Legend
    draw.rectangle([(30, h - 140), (w - 30, h - 30)], fill=(255, 255, 255, 240), outline=C_GRID, width=2)
    draw.text((45, h - 130), "EmCAD સિક્વિન કન્ફિગરેશન: Position: Expand/Contract To Fit | Fix Type 26", font=font_s, fill=C_NAVY)
    draw.text((45, h - 100), "• ઓવરલેપિંગ વર્તુળ = માછલીની છાલ જેવો Overlap Sew લુક (સિક્વિન એકબીજા પર ચડે છે)", font=font_xs, fill=C_TEXT)
    draw.text((45, h - 75), "• લાલ ટાંકા = ૩-પોઇન્ટ લોક ટાંકો (Tie Stitch) જેથી ધોવાયા પછી ટિકી નીકળી ન જાય", font=font_xs, fill=C_MUTED)

    return img

def draw_vector_beads(w, h):
    """Draws a vector Beads schematic showing round pearls & cutdana pipe spacing"""
    img = Image.new('RGB', (w, h), (250, 252, 255))
    draw = ImageDraw.Draw(img)
    
    for x in range(0, w, 40):
        draw.line([(x, 0), (x, h)], fill=(235, 240, 248), width=1)
    for y in range(0, h, 40):
        draw.line([(y, 0), (y, h)], fill=(235, 240, 248), width=1)
        
    font_s = get_font(20)
    font_xs = get_font(16)
    
    # Top track: Beads A (Round Pearls 2.0 mm, Taka = 2.30 mm)
    y1 = h // 3
    draw.text((50, y1 - 70), "Track 1: Beads A (Round Pearls - ગોળ મોતી 2.0mm)", font=font_s, fill=C_BLUE)
    draw.text((50, y1 - 45), "Machine Taka (ટાંકો લંબાઈ) = 2.30 mm", font=font_xs, fill=C_MUTED)
    draw.line([(50, y1), (w - 50, y1)], fill=(180, 195, 215), width=2)
    
    step_p = 80
    for px in range(120, w - 100, step_p):
        # Round Pearl
        draw.ellipse([(px - 22, y1 - 22), (px + 22, y1 + 22)], fill=(255, 255, 255), outline=C_BLUE, width=3)
        # Needle puncture stitches on both sides
        draw.line([(px - 38, y1), (px - 22, y1)], fill=C_RED, width=3)
        draw.line([(px + 22, y1), (px + 38, y1)], fill=C_RED, width=3)
        draw.ellipse([(px - 38 - 3, y1 - 3), (px - 38 + 3, y1 + 3)], fill=C_RED)
        draw.ellipse([(px + 38 - 3, y1 - 3), (px + 38 + 3, y1 + 3)], fill=C_RED)
        
    # Dimension line on Track 1
    draw.line([(280, y1 + 35), (360, y1 + 35)], fill=C_GOLD, width=2)
    draw.line([(280, y1 + 25), (280, y1 + 45)], fill=C_GOLD, width=2)
    draw.line([(360, y1 + 25), (360, y1 + 45)], fill=C_GOLD, width=2)
    draw.text((290, y1 + 42), "2.30 mm", font=font_xs, fill=C_GOLD)
    
    # Bottom track: Beads B (Bugle Pipe / Cutdana 4.0 mm, Taka = 4.50 mm)
    y2 = (h * 2) // 3
    draw.text((50, y2 - 70), "Track 2: Beads B (Cutdana Bugle Pipe - કાચની નળી 4.0mm)", font=font_s, fill=C_GREEN)
    draw.text((50, y2 - 45), "Machine Taka (ટાંકો લંબાઈ) = 4.50 mm | Angle: Alt+CapsLock 9°", font=font_xs, fill=C_MUTED)
    draw.line([(50, y2), (w - 50, y2)], fill=(180, 195, 215), width=2)
    
    step_b = 130
    for bx in range(130, w - 120, step_b):
        # Long cylindrical glass pipe
        draw.rounded_rectangle([(bx - 40, y2 - 14), (bx + 40, y2 + 14)], radius=5, fill=(255, 245, 210), outline=C_GREEN, width=3)
        # Through hole and needle thread entering/exiting
        draw.line([(bx - 55, y2), (bx - 40, y2)], fill=C_RED, width=3)
        draw.line([(bx + 40, y2), (bx + 55, y2)], fill=C_RED, width=3)
        draw.ellipse([(bx - 55 - 3, y2 - 3), (bx - 55 + 3, y2 + 3)], fill=C_RED)
        draw.ellipse([(bx + 55 - 3, y2 - 3), (bx + 55 + 3, y2 + 3)], fill=C_RED)
        
    # Dimension line on Track 2
    draw.line([(390, y2 + 30), (520, y2 + 30)], fill=C_GOLD, width=2)
    draw.line([(390, y2 + 20), (390, y2 + 40)], fill=C_GOLD, width=2)
    draw.line([(520, y2 + 20), (520, y2 + 40)], fill=C_GOLD, width=2)
    draw.text((425, y2 + 36), "4.50 mm Taka", font=font_xs, fill=C_GOLD)
    
    # Legend
    draw.rectangle([(30, h - 140), (w - 30, h - 30)], fill=(255, 255, 255, 240), outline=C_GRID, width=2)
    draw.text((45, h - 130), "EmCAD બીડ્સ માસ્ટર નિયમો: Arrange -> Break Down (Alt+Y Cut / Alt+B Split)", font=font_s, fill=C_NAVY)
    draw.text((45, h - 100), "• Short Stitches = 0.5 mm: ખૂણા પર સોય કાચની નળી સાથે અથડાઈને તૂટતી અટકાવવા", font=font_xs, fill=C_TEXT)
    draw.text((45, h - 75), "• Alt + CapsLock = બીડ્સને ૯ ડિગ્રી ના એંગલે ફેરવવા | Fix Adjust = ઓવરલેપિંગ કાણાં સાફ કરવા", font=font_xs, fill=C_MUTED)

    return img

def draw_vector_mirror(w, h):
    """Draws a vector Mirror schematic showing original half, 2-click axis, and reflection"""
    img = Image.new('RGB', (w, h), (250, 252, 255))
    draw = ImageDraw.Draw(img)
    
    for x in range(0, w, 40):
        draw.line([(x, 0), (x, h)], fill=(235, 240, 248), width=1)
    for y in range(0, h, 40):
        draw.line([(y, 0), (y, h)], fill=(235, 240, 248), width=1)
        
    font_s = get_font(20)
    font_xs = get_font(16)
    
    cx, cy = w // 2, h // 2
    
    # Central Mirror Axis Line
    draw.line([(cx, 60), (cx, h - 160)], fill=C_RED, width=4)
    # 2 Click indicators
    draw.ellipse([(cx - 8, 100 - 8), (cx + 8, 100 + 8)], fill=C_RED, outline=C_WHITE, width=2)
    draw.text((cx + 15, 90), "Click 1 (Start of Axis)", font=font_xs, fill=C_RED)
    draw.ellipse([(cx - 8, h - 200 - 8), (cx + 8, h - 200 + 8)], fill=C_RED, outline=C_WHITE, width=2)
    draw.text((cx + 15, h - 210), "Click 2 (End of Axis)", font=font_xs, fill=C_RED)
    
    # Left Half: Original Vector Drawing (Solid Blue)
    # Right Half: Mirrored Copy (Dashed / Gold)
    petals = 6
    for i in range(petals):
        angle_l = math.radians(110 + i * 25)
        angle_r = math.radians(70 - i * 25)
        
        # Left petal center
        lx = cx - 180 * math.sin(angle_l)
        ly = cy - 140 * math.cos(angle_l)
        draw.ellipse([(lx - 35, ly - 22), (lx + 35, ly + 22)], fill=(225, 240, 255), outline=C_BLUE, width=3)
        draw.line([(cx, cy), (lx, ly)], fill=C_BLUE, width=2)
        
        # Right petal center (Mirrored)
        rx = cx + 180 * math.sin(angle_l)
        ry = cy - 140 * math.cos(angle_l)
        draw.ellipse([(rx - 35, ry - 22), (rx + 35, ry + 22)], fill=(255, 245, 220), outline=C_GOLD, width=3)
        draw.line([(cx, cy), (rx, ry)], fill=C_GOLD, width=2)

    # Paisley curve left
    k_left = [(cx - 20, cy + 120), (cx - 120, cy + 180), (cx - 180, cy + 100), (cx - 100, cy + 20), (cx - 30, cy + 60)]
    k_right = [(cx + 20, cy + 120), (cx + 120, cy + 180), (cx + 180, cy + 100), (cx + 100, cy + 20), (cx + 30, cy + 60)]
    draw.line(k_left, fill=C_BLUE, width=4)
    draw.line(k_right, fill=C_GOLD, width=4)
    
    draw.text((cx - 280, 120), "ORIGINAL (મૂળ ડ્રોઇંગ)", font=font_s, fill=C_BLUE)
    draw.text((cx + 80, 120), "MIRRORED ('R' કી પ્રતિબિંબ)", font=font_s, fill=C_GOLD)
    
    # Legend
    draw.rectangle([(30, h - 140), (w - 30, h - 30)], fill=(255, 255, 255, 240), outline=C_GRID, width=2)
    draw.text((45, h - 130), "EmCAD મિરરિંગ કમાન્ડ: 'R' Key -> Center Axis પર ૨ ક્લિક આપવી", font=font_s, fill=C_NAVY)
    draw.text((45, h - 100), "• આડી ક્લિક = ઉપર/નીચે પ્રતિબિંબ  |  • ઊભી ક્લિક = ડાબે/જમણે ૧૦૦% સરખી નકલ", font=font_xs, fill=C_TEXT)
    draw.text((45, h - 75), "• Step 15 સાડી પંચિંગ: ૪૦૦ mm એરિયામાં ૫૬૦ mm સેન્ટર પર પલ્લુ મિરર લોક થાય છે", font=font_xs, fill=C_MUTED)

    return img

def draw_vector_shading(w, h):
    """Draws a vector Shading / Tatami schematic showing contours & 90 deg fill angles"""
    img = Image.new('RGB', (w, h), (250, 252, 255))
    draw = ImageDraw.Draw(img)
    
    for x in range(0, w, 40):
        draw.line([(x, 0), (x, h)], fill=(235, 240, 248), width=1)
    for y in range(0, h, 40):
        draw.line([(y, 0), (y, h)], fill=(235, 240, 248), width=1)
        
    font_s = get_font(20)
    font_xs = get_font(16)
    
    cx, cy = w // 2, h // 2 - 30
    
    # Draw large shaded flower petal
    r = 200
    # Base dark red zone
    draw.pieslice([(cx - r, cy - r), (cx + r, cy + r)], 210, 330, fill=(255, 225, 230), outline=C_RED, width=3)
    # Tatami lines in base zone
    for y in range(cy - 120, cy, 14):
        draw.line([(cx - 110, y), (cx + 110, y)], fill=C_RED, width=2)
    draw.text((cx - 80, cy - 70), "Needle 1: Dark Red Base (તળિયું)", font=font_xs, fill=C_RED)
    
    # Middle pink gradient zone
    draw.pieslice([(cx - r + 30, cy - r - 40), (cx + r - 30, cy + r - 40)], 220, 320, fill=(255, 240, 245), outline=C_MAGENTA, width=2)
    # Perpendicular 90 deg fill lines
    for x in range(cx - 70, cx + 80, 16):
        draw.line([(x, cy - 170), (x, cy - 80)], fill=C_MAGENTA, width=2)
    draw.text((cx - 90, cy - 140), "Needle 2: 90° Perpendicular Fill", font=font_xs, fill=C_MAGENTA)
    
    # Outer light ivory edge
    draw.arc([(cx - r - 10, cy - r - 60), (cx + r + 10, cy + r - 60)], 210, 330, fill=C_GOLD, width=4)
    draw.text((cx - 80, cy - 230), "Needle 3: Ivory Tip Gradient (કિનારી)", font=font_xs, fill=C_GOLD)
    
    # Florentine curved angle lines indicator
    draw.arc([(cx - 150, cy - 10), (cx + 150, cy + 180)], 190, 350, fill=C_BLUE, width=3)
    draw.text((cx - 120, cy + 90), "Florentine Effect (મોજા જેવો વળાંક)", font=font_s, fill=C_BLUE)

    # Legend
    draw.rectangle([(30, h - 140), (w - 30, h - 30)], fill=(255, 255, 255, 240), outline=C_GRID, width=2)
    draw.text((45, h - 130), "EmCAD શેડિંગ ટેકનિક: ૯-સોય મશીન કલર સિક્વન્સિંગ (Keys 1 to 6)", font=font_s, fill=C_NAVY)
    draw.text((45, h - 100), "• Perpendicular Fill = ૯૦ ડિગ્રી પરપેન્ડીક્યુલર તતામીથી સૂર્યપ્રકાશમાં ડબલ-શેડ ચમક", font=font_xs, fill=C_TEXT)
    draw.text((45, h - 75), "• Florentine Effect = વળાંકવાળી એંગલ લાઇન વડે કુદરતી પાંદડી જેવો 3D વેવ લુક", font=font_xs, fill=C_MUTED)

    return img

def draw_vector_cording(w, h):
    """Draws a vector Cording / Dori schematic showing core run guide and zigzag tacking"""
    img = Image.new('RGB', (w, h), (250, 252, 255))
    draw = ImageDraw.Draw(img)
    
    for x in range(0, w, 40):
        draw.line([(x, 0), (x, h)], fill=(235, 240, 248), width=1)
    for y in range(0, h, 40):
        draw.line([(y, 0), (y, h)], fill=(235, 240, 248), width=1)
        
    font_s = get_font(20)
    font_xs = get_font(16)
    
    cx, cy = w // 2, h // 2 - 30
    
    # Draw thick golden core dori (center cord)
    cord_pts = []
    for x in range(80, w - 80, 10):
        y = cy + 100 * math.sin((x - 80) * 0.012)
        cord_pts.append((x, y))
        
    # Draw thick cord shadow & body
    draw.line(cord_pts, fill=(180, 130, 20), width=18)
    draw.line(cord_pts, fill=(245, 200, 60), width=12)
    draw.line(cord_pts, fill=(255, 240, 160), width=4)
    
    # Zigzag tacking stitch across the cord (Angle 50, 35, 21; Times 2)
    step_z = 24
    for i in range(0, len(cord_pts) - 3, 2):
        p = cord_pts[i]
        # Zigzag stitch perpendicular
        draw.line([(p[0] - 12, p[1] - 18), (p[0] + 12, p[1] + 18)], fill=C_RED, width=3)
        draw.ellipse([(p[0] - 12 - 3, p[1] - 18 - 3), (p[0] - 12 + 3, p[1] - 18 + 3)], fill=C_RED)
        draw.ellipse([(p[0] + 12 - 3, p[1] + 18 - 3), (p[0] + 12 + 3, p[1] + 18 + 3)], fill=C_RED)
        
    draw.text((150, cy - 110), "Core Cord (મુખ્ય જાડી દોરી)", font=font_s, fill=C_GOLD)
    draw.line([(240, cy - 90), (280, cy - 20)], fill=C_GOLD, width=2)
    
    draw.text((w - 380, cy + 90), "Zigzag Tack Stitch (ટાંકવા માટે)", font=font_s, fill=C_RED)
    draw.text((w - 380, cy + 115), "Angle: 50, 35, 21 | Times: 2", font=font_xs, fill=C_MUTED)
    draw.line([(w - 240, cy + 85), (w - 260, cy + 25)], fill=C_RED, width=2)
    
    # Legend
    draw.rectangle([(30, h - 140), (w - 30, h - 30)], fill=(255, 255, 255, 240), outline=C_GRID, width=2)
    draw.text((45, h - 130), "EmCAD કોર્ડિંગ સેટિંગ: F12 Cording Tool | Angle = 50, 35, 21; Times = 2", font=font_s, fill=C_NAVY)
    draw.text((45, h - 100), "• સોય દોરીને કાપ્યા વગર બંને બાજુ ઝિગઝેગ ટાંકા મારીને કાપડ સાથે જકડી રાખે છે", font=font_xs, fill=C_TEXT)
    draw.text((45, h - 75), "• Start / End Lock: શરૂઆત અને છેડે રન સ્ટીચથી પેક કરવું જેથી દોરી નીકળી ન જાય", font=font_xs, fill=C_MUTED)

    return img

def create_board(title_gu, title_en, vector_img, real_img_path, filename):
    """Combines vector schematic (left) and real embroidery photo (right) into a master 2200x1250 board"""
    bw = 2200
    bh = 1250
    header_h = 110
    panel_w = 1040
    panel_h = 1060
    
    board = Image.new('RGB', (bw, bh), C_NAVY)
    draw = ImageDraw.Draw(board)
    
    # Top Header
    font_title = get_font(32)
    font_sub = get_font(20)
    font_badge = get_font(18)
    
    # Header bar
    draw.rectangle([(0, 0), (bw, header_h)], fill=C_DARK)
    draw.rectangle([(0, header_h - 4), (bw, header_h)], fill=C_GOLD)
    
    draw.text((40, 20), title_gu, font=font_title, fill=C_WHITE)
    draw.text((40, 68), title_en, font=font_sub, fill=(203, 213, 225))
    
    # Badge right
    draw.rounded_rectangle([(bw - 380, 28), (bw - 40, 82)], radius=8, fill=(217, 119, 6, 40), outline=C_GOLD, width=2)
    draw.text((bw - 360, 42), "DRAWING vs REAL DESIGN", font=font_badge, fill=C_GOLD)
    
    # Left Panel: EmCAD Vector Schematic
    vec_resized = vector_img.resize((panel_w, panel_h), Image.Resampling.LANCZOS)
    board.paste(vec_resized, (40, header_h + 30))
    # Border for Left Panel
    draw.rectangle([(40, header_h + 30), (40 + panel_w, header_h + 30 + panel_h)], outline=C_BLUE, width=3)
    # Header Tag Left
    draw.rectangle([(40, header_h + 30), (40 + 380, header_h + 75)], fill=C_BLUE)
    draw.text((55, header_h + 40), "📐 EmCAD Vector / ડ્રોઇંગ", font=get_font(22), fill=C_WHITE)
    
    # Right Panel: Real Embroidered Photo
    real_im = Image.open(real_img_path)
    real_im = ImageOps.fit(real_im, (panel_w, panel_h), Image.Resampling.LANCZOS)
    board.paste(real_im, (bw - panel_w - 40, header_h + 30))
    # Border for Right Panel
    draw.rectangle([(bw - panel_w - 40, header_h + 30), (bw - 40, header_h + 30 + panel_h)], outline=C_GOLD, width=3)
    # Header Tag Right
    draw.rectangle([(bw - panel_w - 40, header_h + 30), (bw - panel_w - 40 + 440, header_h + 75)], fill=C_GOLD)
    draw.text((bw - panel_w - 25, header_h + 40), "🧵 વાસ્તવિક મશીન સ્ટીચ (Real Stitched Fabric)", font=get_font(20), fill=C_DARK)
    
    out_path = os.path.join(ASSET_DIR, filename)
    board.save(out_path, quality=95)
    print(f"Created comparison board: {filename} ({board.size})")
    return out_path

def main():
    print("Building all 6 Visual Comparison Boards...")
    
    # 1. Paghdi
    vec_paghdi = draw_vector_paghdi(1040, 1060)
    create_board(
        "પાઘડી (Paghdi / Column Symmetry F4) - સંપૂર્ણ સરખામણી",
        "EmCAD Vector Column Nodes vs Real Embroidered Satin Stitch Design",
        vec_paghdi,
        REAL_PAGHDI,
        "69_Compare_Paghdi_Vector_Drawing_vs_Real_Satin_Stitch.jpg"
    )

    # 2. Sequin
    vec_seq = draw_vector_sequin(1040, 1060)
    create_board(
        "સિક્વિન (Sequin / ટિકી વર્ક) - સંપૂર્ણ સરખામણી",
        "EmCAD Sequin Drop Path & Fix Type 26 vs Real Overlapping Metallic Sequins",
        vec_seq,
        REAL_SEQUIN,
        "70_Compare_Sequin_Vector_Drawing_vs_Real_Embroidery.jpg"
    )

    # 3. Beads
    vec_beads = draw_vector_beads(1040, 1060)
    create_board(
        "બીડ્સ (Beads / મોતી અને કટદાણા) - સંપૂર્ણ સરખામણી",
        "EmCAD Beads Spacing & Taka Table vs Real Glass Pearls & Cutdana Beads",
        vec_beads,
        REAL_BEADS,
        "71_Compare_Beads_Vector_Drawing_vs_Real_Embroidery.jpg"
    )

    # 4. Mirror
    vec_mirror = draw_vector_mirror(1040, 1060)
    create_board(
        "મિરરિંગ (Mirror 'R' Key) - સંપૂર્ણ સરખામણી",
        "EmCAD 2-Click Mirror Axis vs Real Symmetrical Embroidered Motif",
        vec_mirror,
        REAL_MIRROR,
        "72_Compare_Mirror_Vector_Drawing_vs_Real_Embroidery.jpg"
    )

    # 5. Shading Flower
    vec_shading = draw_vector_shading(1040, 1060)
    create_board(
        "શેડિંગ ફ્લાવર (Shading Flower & Tatami Fill) - સંપૂર્ણ સરખામણી",
        "EmCAD 90° Perpendicular Fill & Color Sequence vs Real Gradient Embroidered Flower",
        vec_shading,
        REAL_SHADED,
        "73_Compare_Shading_Flower_Vector_Drawing_vs_Real_Embroidery.jpg"
    )

    # 6. Cording
    vec_cording = draw_vector_cording(1040, 1060)
    create_board(
        "કોર્ડિંગ (Cording F12 દોરી વર્ક) - સંપૂર્ણ સરખામણી",
        "EmCAD Core Cord & Zigzag Tack Stitch vs Real Raised 3D Dori Embroidery",
        vec_cording,
        REAL_CORDING,
        "74_Compare_Cording_Dori_Vector_Drawing_vs_Real_Embroidery.jpg"
    )

    print("All 6 comparison boards generated successfully in emCad_organized_assets!")

if __name__ == '__main__':
    main()
