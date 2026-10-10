#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Refined High-Quality Educational Animated GIFs for EmCAD:
1. anim_jump_stitching_simulation.gif: Needle stitching, Stop, Trim Scissor, and dotted Jump line.
2. anim_sequin_overlap_lock.gif: Sequin disc dropping with authentic 40% fish-scale overlap, needle penetrating center hole, Fix Type 26 triangle lock.
3. anim_beads_taka_placement.gif: Pearl beads and cutdana glass pipes with taka distance and 9-deg tilt.
4. anim_paghdi_column_stitching.gif: Column symmetry F4 satin fill, boundary rails, and angle lines.
5. anim_lock_origin_dr250.gif: Start Tie-in lock, motif stitching, End Tie-off lock, trim, and DR 250 Origin return.
"""

import os
import math
from PIL import Image, ImageDraw, ImageFont

WORKSPACE = '/Users/manavramani/Desktop/emCad_explain_software'
ASSET_DIR = os.path.join(WORKSPACE, 'emCad_organized_assets')
FONT_PATH = '/Library/Fonts/Arial Unicode.ttf'

def get_font(size):
    try:
        return ImageFont.truetype(FONT_PATH, size)
    except:
        return ImageFont.load_default()

# Base Colors
C_DARK = (15, 23, 42)
C_NAVY = (15, 41, 74)
C_WHITE = (255, 255, 255)
C_GRID = (226, 232, 240)
C_GOLD = (217, 119, 6)
C_RED = (220, 38, 38)
C_GREEN = (5, 150, 105)
C_BLUE = (37, 99, 235)
C_LIGHT_BG = (248, 250, 252)

# --- 1. JUMP & STITCHING ANIMATION ---
def make_jump_animation():
    w, h = 800, 480
    frames = []
    total_steps = 42
    
    font_title = get_font(20)
    font_bold = get_font(16)
    font_sm = get_font(13)
    
    for frame_idx in range(total_steps):
        img = Image.new('RGB', (w, h), (252, 253, 255))
        draw = ImageDraw.Draw(img)
        
        # Grid
        for x in range(0, w, 40):
            draw.line([(x, 50), (x, h - 50)], fill=C_GRID, width=1)
        for y in range(50, h - 50, 40):
            draw.line([(0, y), (w, y)], fill=C_GRID, width=1)
            
        # Top banner
        draw.rectangle([(0, 0), (w, 48)], fill=C_NAVY)
        draw.text((20, 12), "EmCAD સિમ્યુલેશન: મશીન સ્ટીચિંગ vs જમ્પ (Stitch vs Jump Mechanics)", font=font_title, fill=C_WHITE)
        
        # Legend (No raw emoji boxes)
        draw.rectangle([(30, 60), (770, 95)], fill=(241, 245, 249), outline=(203, 213, 225))
        draw.line([(50, 78), (90, 78)], fill=C_RED, width=4)
        draw.text((100, 70), "લાલ ઘાટી લાઇન = સ્ટીચિંગ (Stitch)", font=font_sm, fill=C_DARK)
        
        for dx in range(320, 360, 8):
            draw.line([(dx, 78), (dx + 4, 78)], fill=C_BLUE, width=3)
        draw.text((370, 70), "વાદળી તૂટક લાઇન = જમ્પ (Jump - સોય ઊંચી)", font=font_sm, fill=C_DARK)
        
        draw.rectangle([(620, 68), (665, 88)], fill=C_GOLD)
        draw.text((626, 71), "TRIM", font=ImageFont.truetype(FONT_PATH, 11), fill=C_WHITE)
        draw.text((675, 70), "= દોરો કાપવો (Auto Trim)", font=font_sm, fill=C_DARK)
        
        # Object 1 area
        draw.rectangle([(60, 180), (250, 300)], outline=(148, 163, 184), width=1)
        draw.text((70, 155), "ઓબ્જેક્ટ ૧ (Flower Leaf)", font=font_sm, fill=C_DARK)
        
        # Object 2 area
        draw.rectangle([(520, 180), (710, 300)], outline=(148, 163, 184), width=1)
        draw.text((530, 155), "ઓબ્જેક્ટ ૨ (Paisley Keri)", font=font_sm, fill=C_DARK)
        
        # Draw Object 1 stitches
        obj1_progress = min(1.0, frame_idx / 15.0)
        num_pts1 = int(obj1_progress * 16)
        for i in range(num_pts1):
            px = 80 + i * 10
            py_top = 200 + (i % 2) * 80
            py_bot = py_top + 20
            draw.line([(px, py_top), (px, py_bot)], fill=C_RED, width=3)
            if i > 0:
                prev_x = 80 + (i - 1) * 10
                prev_py = 200 + ((i - 1) % 2) * 80 + 20
                draw.line([(prev_x, prev_py), (px, py_top)], fill=C_RED, width=2)
                
        # Trim box
        if frame_idx >= 15:
            draw.rectangle([(235, 225), (315, 255)], fill=(254, 243, 199), outline=C_GOLD, width=2)
            draw.text((245, 232), "[TRIM]", font=font_bold, fill=C_GOLD)
            
        # Draw Jump Line
        if frame_idx >= 18:
            jump_progress = min(1.0, (frame_idx - 18) / 12.0)
            max_jump_x = 240 + int(jump_progress * 290)
            for jx in range(240, max_jump_x, 10):
                draw.line([(jx, 240), (jx + 5, 240)], fill=C_BLUE, width=3)
                
        # Draw Object 2 stitches
        if frame_idx >= 30:
            obj2_progress = min(1.0, (frame_idx - 30) / 11.0)
            num_pts2 = int(obj2_progress * 16)
            for i in range(num_pts2):
                px = 540 + i * 10
                py_top = 200 + (i % 2) * 80
                py_bot = py_top + 20
                draw.line([(px, py_top), (px, py_bot)], fill=C_RED, width=3)
                if i > 0:
                    prev_x = 540 + (i - 1) * 10
                    prev_py = 200 + ((i - 1) % 2) * 80 + 20
                    draw.line([(prev_x, prev_py), (px, py_top)], fill=C_RED, width=2)
                    
        # Needle Position
        if frame_idx < 15:
            nx = 80 + num_pts1 * 10
            ny = 220
            status_text = "STATUS: STITCHING (ટાંકો પડે છે - દોરો સક્રિય)"
            status_col = C_RED
        elif frame_idx < 19:
            nx = 240
            ny = 240
            status_text = "STATUS: THREAD TRIM (દોરો કપાઈ રહ્યો છે)"
            status_col = C_GOLD
        elif frame_idx < 30:
            nx = 240 + int(((frame_idx - 18) / 12.0) * 290)
            ny = 240
            status_text = "STATUS: JUMPING (સોય ઊંચી - ફ્રેમ ઝડપથી ખસે છે)"
            status_col = C_BLUE
        else:
            nx = 540 + num_pts2 * 10
            ny = 220
            status_text = "STATUS: STITCHING OBJECT 2 (નવો ઓબ્જેક્ટ શરૂ)"
            status_col = C_GREEN
            
        # Draw needle
        draw.polygon([(nx, ny), (nx - 8, ny - 25), (nx + 8, ny - 25)], fill=(100, 116, 139))
        draw.line([(nx, ny - 25), (nx, ny - 50)], fill=(71, 85, 105), width=3)
        draw.ellipse([(nx - 4, ny - 4), (nx + 4, ny + 4)], fill=C_GOLD)
        
        # Bottom Status Bar
        draw.rectangle([(0, h - 45), (w, h)], fill=C_DARK)
        draw.text((20, h - 32), status_text, font=font_bold, fill=status_col)
        draw.text((540, h - 32), f"Needle Position: X={nx} mm, Y={ny} mm", font=font_sm, fill=(203, 213, 225))
        
        frames.append(img)
        
    out_path = os.path.join(ASSET_DIR, 'anim_jump_stitching_simulation.gif')
    frames[0].save(out_path, save_all=True, append_images=frames[1:], duration=150, loop=0)
    print(f"Updated: {out_path}")

# --- 2. SEQUIN DROP & FIX TYPE 26 WITH TRUE OVERLAP ---
def make_sequin_animation():
    w, h = 800, 480
    frames = []
    
    font_title = get_font(20)
    font_bold = get_font(16)
    font_sm = get_font(13)
    
    # 8 sequin centers with authentic 42px spacing and radius 34 (overlapping ~40%)
    centers = []
    for i in range(8):
        cx = 90 + i * 80
        cy = 230 + int(20 * math.sin(i * 0.5))
        centers.append((cx, cy))
    r = 34
    
    total_steps = len(centers) * 5 + 4
    
    for frame_idx in range(total_steps):
        img = Image.new('RGB', (w, h), (250, 252, 255))
        draw = ImageDraw.Draw(img)
        
        # Background Grid
        for x in range(0, w, 40):
            draw.line([(x, 50), (x, h - 50)], fill=C_GRID, width=1)
        for y in range(50, h - 50, 40):
            draw.line([(0, y), (w, y)], fill=C_GRID, width=1)
            
        # Top banner
        draw.rectangle([(0, 0), (w, 48)], fill=C_NAVY)
        draw.text((20, 12), "EmCAD સિમ્યુલેશન: સિક્વિન (ટિકી) ડ્રોપ અને Fix Type 26 ત્રિકોણ લોક", font=font_title, fill=C_WHITE)
        
        # Legend
        draw.rectangle([(30, 60), (770, 95)], fill=(241, 245, 249), outline=(203, 213, 225))
        draw.text((40, 70), "• ગોલ્ડન પતરી (Sequin 3mm)", font=font_sm, fill=C_DARK)
        draw.text((240, 70), "• Fix Type 26: ૩-પોઇન્ટ ત્રિકોણ લોક (120° Tie Stitch)", font=font_sm, fill=C_DARK)
        draw.text((580, 70), "• Overlap Sew: 40% માછલીની છાલ", font=font_sm, fill=C_DARK)
        
        active_seq_idx = min(len(centers) - 1, frame_idx // 5)
        sub_step = frame_idx % 5
        
        # Draw all completed sequins
        for i in range(active_seq_idx):
            cx, cy = centers[i]
            # Outer disc
            draw.ellipse([(cx - r, cy - r), (cx + r, cy + r)], fill=(254, 240, 138), outline=(202, 138, 4), width=2)
            # Center hole
            draw.ellipse([(cx - 6, cy - 6), (cx + 6, cy + 6)], fill=C_WHITE, outline=(161, 98, 7), width=1)
            # Fix Type 26
            for angle in [90, 210, 330]:
                rad = math.radians(angle)
                tx = cx + int((r - 5) * math.cos(rad))
                ty = cy + int((r - 5) * math.sin(rad))
                draw.line([(cx, cy), (tx, ty)], fill=C_RED, width=3)
                draw.ellipse([(tx - 3, ty - 3), (tx + 3, ty + 3)], fill=C_RED)
                
        # Current active sequin
        cx, cy = centers[active_seq_idx]
        
        if sub_step >= 1:
            draw.ellipse([(cx - r, cy - r), (cx + r, cy + r)], fill=(254, 240, 138), outline=(202, 138, 4), width=2)
            draw.ellipse([(cx - 6, cy - 6), (cx + 6, cy + 6)], fill=C_WHITE, outline=(161, 98, 7), width=1)
            
        angles = [90, 210, 330]
        for a_i, angle in enumerate(angles):
            if sub_step >= (2 + a_i):
                rad = math.radians(angle)
                tx = cx + int((r - 5) * math.cos(rad))
                ty = cy + int((r - 5) * math.sin(rad))
                draw.line([(cx, cy), (tx, ty)], fill=C_RED, width=3)
                draw.ellipse([(tx - 3, ty - 3), (tx + 3, ty + 3)], fill=C_RED)
                
        # Needle position
        if sub_step == 0:
            nx, ny = cx, cy - 45
            status_text = f"SEQUIN #{active_seq_idx + 1}: FEEDER DROPPING METALLIC DISC"
        elif sub_step == 1:
            nx, ny = cx, cy
            status_text = f"SEQUIN #{active_seq_idx + 1}: NEEDLE PENETRATING CENTER HOLE"
        elif sub_step == 2:
            rad = math.radians(90)
            nx, ny = cx + int((r - 5) * math.cos(rad)), cy + int((r - 5) * math.sin(rad))
            status_text = f"SEQUIN #{active_seq_idx + 1}: LOCK POINT 1 (BOTTOM TIE)"
        elif sub_step == 3:
            rad = math.radians(210)
            nx, ny = cx + int((r - 5) * math.cos(rad)), cy + int((r - 5) * math.sin(rad))
            status_text = f"SEQUIN #{active_seq_idx + 1}: LOCK POINT 2 (LEFT TIE)"
        else:
            rad = math.radians(330)
            nx, ny = cx + int((r - 5) * math.cos(rad)), cy + int((r - 5) * math.sin(rad))
            status_text = f"SEQUIN #{active_seq_idx + 1}: LOCK POINT 3 (RIGHT TIE - LOCKED!)"
            
        # Draw needle
        draw.polygon([(nx, ny), (nx - 7, ny - 22), (nx + 7, ny - 22)], fill=(100, 116, 139))
        draw.line([(nx, ny - 22), (nx, ny - 45)], fill=(71, 85, 105), width=3)
        draw.ellipse([(nx - 4, ny - 4), (nx + 4, ny + 4)], fill=C_GOLD)
        
        # Bottom status
        draw.rectangle([(0, h - 45), (w, h)], fill=C_DARK)
        draw.text((20, h - 32), f"STATUS: {status_text}", font=font_bold, fill=C_GOLD)
        draw.text((540, h - 32), "Fix Type 26 (ત્રિકોણ લોક)", font=font_bold, fill=C_WHITE)
        
        frames.append(img)
        
    out_path = os.path.join(ASSET_DIR, 'anim_sequin_overlap_lock.gif')
    frames[0].save(out_path, save_all=True, append_images=frames[1:], duration=150, loop=0)
    print(f"Updated: {out_path}")

# --- 3. BEADS ANIMATION ---
def make_beads_animation():
    w, h = 800, 480
    frames = []
    total_steps = 38
    
    font_title = get_font(20)
    font_bold = get_font(16)
    font_sm = get_font(13)
    
    for frame_idx in range(total_steps):
        img = Image.new('RGB', (w, h), (252, 253, 255))
        draw = ImageDraw.Draw(img)
        
        # Grid
        for x in range(0, w, 40):
            draw.line([(x, 50), (x, h - 50)], fill=C_GRID, width=1)
        for y in range(50, h - 50, 40):
            draw.line([(0, y), (w, y)], fill=C_GRID, width=1)
            
        # Top banner
        draw.rectangle([(0, 0), (w, 48)], fill=C_NAVY)
        draw.text((20, 12), "EmCAD સિમ્યુલેશન: બીડ્સ (મોતી & કટદાણા) ટાંકો અને ૯° રોટેશન", font=font_title, fill=C_WHITE)
        
        # Legend
        draw.rectangle([(30, 60), (770, 95)], fill=(241, 245, 249), outline=(203, 213, 225))
        draw.text((40, 70), "• Track 1: ગોળ મોતી (Pearl 2.0mm) | Taka = 2.30mm", font=font_sm, fill=C_DARK)
        draw.text((430, 70), "• Track 2: કાચની નળી (Cutdana 4.0mm) | Taka = 4.50mm", font=font_sm, fill=C_DARK)
        
        # Track 1
        draw.line([(60, 190), (740, 190)], fill=(148, 163, 184), width=2)
        draw.text((60, 140), "Track 1: Beads A (ગોળ મોતી) - Spacing: 2.30 mm", font=font_bold, fill=C_NAVY)
        
        num_pearls = min(8, frame_idx // 2)
        for p in range(num_pearls):
            px = 100 + p * 75
            draw.ellipse([(px - 16, 190 - 16), (px + 16, 190 + 16)], fill=(248, 250, 252), outline=(30, 96, 145), width=2)
            draw.ellipse([(px - 4, 190 - 6), (px + 2, 190)], fill=C_WHITE)
            draw.ellipse([(px - 22, 190 - 3), (px - 16, 190 + 3)], fill=C_RED)
            draw.ellipse([(px + 16, 190 - 3), (px + 22, 190 + 3)], fill=C_RED)
            draw.line([(px - 37, 190), (px - 19, 190)], fill=C_RED, width=2)
            
        # Track 2
        draw.line([(60, 330), (740, 330)], fill=(148, 163, 184), width=2)
        draw.text((60, 280), "Track 2: Beads B (કટદાણા કાચની નળી) - Spacing: 4.50 mm | Alt+CapsLock 9°", font=font_bold, fill=C_GOLD)
        
        num_pipes = min(5, frame_idx // 3)
        for p in range(num_pipes):
            px = 110 + p * 120
            draw.polygon([
                (px - 32, 330 - 10), (px + 32, 330 - 10),
                (px + 32, 330 + 10), (px - 32, 330 + 10)
            ], fill=(254, 240, 138), outline=(202, 138, 4), width=2)
            draw.line([(px - 30, 330), (px + 30, 330)], fill=(161, 98, 7), width=1)
            draw.ellipse([(px - 38, 330 - 3), (px - 32, 330 + 3)], fill=C_RED)
            draw.ellipse([(px + 32, 330 - 3), (px + 38, 330 + 3)], fill=C_RED)
            draw.line([(px - 60, 330), (px - 35, 330)], fill=C_RED, width=2)
            
        if frame_idx < 18:
            nx = 100 + num_pearls * 75
            ny = 190
            status_text = f"PEARL BEAD #{num_pearls + 1}: PUNCHING TAKA 2.30mm"
        else:
            nx = 110 + num_pipes * 120
            ny = 330
            status_text = f"CUTDANA PIPE #{num_pipes + 1}: TAKA 4.50mm | TILT 9°"
            
        draw.polygon([(nx, ny), (nx - 7, ny - 22), (nx + 7, ny - 22)], fill=(100, 116, 139))
        draw.line([(nx, ny - 22), (nx, ny - 45)], fill=(71, 85, 105), width=3)
        draw.ellipse([(nx - 4, ny - 4), (nx + 4, ny + 4)], fill=C_RED)
        
        draw.rectangle([(0, h - 45), (w, h)], fill=C_DARK)
        draw.text((20, h - 32), f"STATUS: {status_text}", font=font_bold, fill=C_GOLD)
        draw.text((530, h - 32), "Break Down: Alt+Y | Split: Alt+B", font=font_sm, fill=(203, 213, 225))
        
        frames.append(img)
        
    out_path = os.path.join(ASSET_DIR, 'anim_beads_taka_placement.gif')
    frames[0].save(out_path, save_all=True, append_images=frames[1:], duration=150, loop=0)
    print(f"Updated: {out_path}")

# --- 4. PAGHDI SATIN ANIMATION ---
def make_paghdi_animation():
    w, h = 800, 480
    frames = []
    total_steps = 38
    
    font_title = get_font(20)
    font_bold = get_font(16)
    font_sm = get_font(13)
    
    cx = w // 2
    pts_left = []
    pts_right = []
    for t in range(0, 180, 5):
        rad = math.radians(t)
        cy = 100 + t * 1.8
        half_w = 40 + 55 * math.sin(rad)
        pts_left.append((cx - half_w, cy))
        pts_right.append((cx + half_w, cy))
        
    for frame_idx in range(total_steps):
        img = Image.new('RGB', (w, h), (252, 253, 255))
        draw = ImageDraw.Draw(img)
        
        for x in range(0, w, 40):
            draw.line([(x, 50), (x, h - 50)], fill=C_GRID, width=1)
        for y in range(50, h - 50, 40):
            draw.line([(0, y), (w, y)], fill=C_GRID, width=1)
            
        draw.rectangle([(0, 0), (w, 48)], fill=C_NAVY)
        draw.text((20, 12), "EmCAD સિમ્યુલેશન: પાઘડી (Paghdi F4) કોલમ સિમેટ્રી સાટિન સ્ટીચિંગ", font=font_title, fill=C_WHITE)
        
        draw.rectangle([(30, 60), (770, 95)], fill=(241, 245, 249), outline=(203, 213, 225))
        draw.text((40, 70), "• વાદળી બાઉન્ડ્રી = Boundary Rails (F4)", font=font_sm, fill=C_DARK)
        draw.text((320, 70), "• પીળા ટાંકા = Satin Stitch Density (0.45mm)", font=font_sm, fill=C_DARK)
        draw.text((620, 70), "• 'D' = તીક્ષ્ણ ખૂણો", font=font_sm, fill=C_DARK)
        
        draw.line([(cx, 95), (cx, 430)], fill=(203, 213, 225), width=2)
        draw.text((cx + 10, 105), "Centerline (X=0)", font=font_sm, fill=(100, 116, 139))
        
        draw.line(pts_left, fill=C_BLUE, width=3)
        draw.line(pts_right, fill=C_BLUE, width=3)
        
        draw.rectangle([(pts_left[0][0] - 6, pts_left[0][1] - 6), (pts_left[0][0] + 6, pts_left[0][1] + 6)], fill=C_RED)
        draw.rectangle([(pts_right[0][0] - 6, pts_right[0][1] - 6), (pts_right[0][0] + 6, pts_right[0][1] + 6)], fill=C_RED)
        draw.text((pts_left[0][0] - 50, pts_left[0][1] - 8), "Node 'D'", font=font_sm, fill=C_RED)
        
        progress = frame_idx / float(total_steps - 1)
        max_idx = int(progress * len(pts_left))
        
        for i in range(0, max_idx, 1):
            p1 = pts_left[i]
            p2 = pts_right[i]
            draw.line([p1, p2], fill=(217, 119, 6), width=3)
            
        if max_idx > 0 and max_idx < len(pts_left):
            if frame_idx % 2 == 0:
                nx, ny = pts_left[max_idx]
            else:
                nx, ny = pts_right[max_idx]
        else:
            nx, ny = cx, 100
            
        draw.polygon([(nx, ny), (nx - 7, ny - 22), (nx + 7, ny - 22)], fill=(100, 116, 139))
        draw.line([(nx, ny - 22), (nx, ny - 45)], fill=(71, 85, 105), width=3)
        draw.ellipse([(nx - 4, ny - 4), (nx + 4, ny + 4)], fill=C_GOLD)
        
        draw.rectangle([(0, h - 45), (w, h)], fill=C_DARK)
        draw.text((20, h - 32), f"STATUS: COLUMN SYMMETRY STITCHING (WIDTH >= 0.8mm)", font=font_bold, fill=C_GOLD)
        draw.text((540, h - 32), f"Stitch Progress: {int(progress * 100)}%", font=font_bold, fill=C_WHITE)
        
        frames.append(img)
        
    out_path = os.path.join(ASSET_DIR, 'anim_paghdi_column_stitching.gif')
    frames[0].save(out_path, save_all=True, append_images=frames[1:], duration=150, loop=0)
    print(f"Updated: {out_path}")

# --- 5. LOCK & ORIGIN DR 250 ANIMATION ---
def make_lock_origin_animation():
    w, h = 800, 480
    frames = []
    total_steps = 38
    
    font_title = get_font(20)
    font_bold = get_font(16)
    font_sm = get_font(13)
    
    origin_x, origin_y = 120, 240
    flower_center_x, flower_center_y = 480, 240
    
    for frame_idx in range(total_steps):
        img = Image.new('RGB', (w, h), (252, 253, 255))
        draw = ImageDraw.Draw(img)
        
        for x in range(0, w, 40):
            draw.line([(x, 50), (x, h - 50)], fill=C_GRID, width=1)
        for y in range(50, h - 50, 40):
            draw.line([(0, y), (w, y)], fill=C_GRID, width=1)
            
        draw.rectangle([(0, 0), (w, 48)], fill=C_NAVY)
        draw.text((20, 12), "EmCAD સિમ્યુલેશન: Tie-in લોક, ટાંકો, Tie-off લોક અને ઓરિજિન DR 250", font=font_title, fill=C_WHITE)
        
        draw.rectangle([(30, 60), (770, 95)], fill=(241, 245, 249), outline=(203, 213, 225))
        draw.text((40, 70), "• Origin DR 250 (X=0, Y=0)", font=font_sm, fill=C_DARK)
        draw.text((260, 70), "• Tie-in Start Lock: 3 ટાંકા ગાંઠ", font=font_sm, fill=C_DARK)
        draw.text((510, 70), "• Tie-off End Lock: 4 ટાંકા પેક + Trim", font=font_sm, fill=C_DARK)
        
        draw.ellipse([(origin_x - 12, origin_y - 12), (origin_x + 12, origin_y + 12)], outline=C_BLUE, width=2)
        draw.line([(origin_x - 18, origin_y), (origin_x + 18, origin_y)], fill=C_BLUE, width=2)
        draw.line([(origin_x, origin_y - 18), (origin_x, origin_y + 18)], fill=C_BLUE, width=2)
        draw.text((origin_x - 45, origin_y + 18), "ORIGIN DR 250 (0,0)", font=font_sm, fill=C_BLUE)
        
        if frame_idx >= 5:
            for jx in range(origin_x + 15, 380, 10):
                draw.line([(jx, 240), (jx + 5, 240)], fill=C_BLUE, width=2)
                
        draw.ellipse([(flower_center_x - 70, flower_center_y - 70), (flower_center_x + 70, flower_center_y + 70)], outline=(203, 213, 225), width=1)
        
        if frame_idx >= 8:
            draw.rectangle([(340, 195), (430, 220)], fill=(236, 253, 245), outline=C_GREEN, width=1)
            draw.text((345, 200), "TIE-IN LOCK", font=font_bold, fill=C_GREEN)
            draw.line([(380, 235), (385, 245)], fill=C_GREEN, width=4)
            draw.line([(385, 245), (380, 245)], fill=C_GREEN, width=4)
            draw.line([(380, 245), (385, 235)], fill=C_GREEN, width=4)
            
        if frame_idx >= 11:
            flower_progress = min(1.0, (frame_idx - 11) / 12.0)
            max_deg = int(flower_progress * 360)
            for deg in range(0, max_deg, 12):
                rad = math.radians(deg)
                fx1 = flower_center_x + int(20 * math.cos(rad))
                fy1 = flower_center_y + int(20 * math.sin(rad))
                fx2 = flower_center_x + int(65 * math.cos(rad))
                fy2 = flower_center_y + int(65 * math.sin(rad))
                draw.line([(fx1, fy1), (fx2, fy2)], fill=C_GOLD, width=3)
                
        if frame_idx >= 24:
            draw.rectangle([(flower_center_x + 40, 195), (flower_center_x + 140, 220)], fill=(254, 242, 242), outline=C_RED, width=1)
            draw.text((flower_center_x + 45, 200), "TIE-OFF LOCK", font=font_bold, fill=C_RED)
            draw.line([(flower_center_x + 70, 235), (flower_center_x + 75, 245)], fill=C_RED, width=4)
            draw.line([(flower_center_x + 75, 245), (flower_center_x + 70, 245)], fill=C_RED, width=4)
            draw.line([(flower_center_x + 70, 245), (flower_center_x + 75, 235)], fill=C_RED, width=4)
            
        if frame_idx >= 28:
            draw.rectangle([(flower_center_x + 75, 240), (flower_center_x + 130, 265)], fill=(254, 243, 199), outline=C_GOLD, width=1)
            draw.text((flower_center_x + 82, 245), "[TRIM]", font=font_bold, fill=C_GOLD)
            
        if frame_idx >= 30:
            ret_progress = min(1.0, (frame_idx - 30) / 5.0)
            cur_ret_x = flower_center_x + 70 - int(ret_progress * (flower_center_x + 70 - origin_x))
            for rx in range(cur_ret_x, flower_center_x + 70, 10):
                draw.line([(rx, 260), (rx + 5, 260)], fill=C_BLUE, width=2)
                
        if frame_idx <= 5:
            nx = origin_x + int((frame_idx / 5.0) * (380 - origin_x))
            ny = 240
            status_text = "MOVE: TRAVELING TO DESIGN START POINT"
            status_col = C_BLUE
        elif frame_idx <= 10:
            nx = 380
            ny = 240
            status_text = "LOCK: TIE-IN START LOCK (૩ ટાંકા ગાંઠ)"
            status_col = C_GREEN
        elif frame_idx <= 22:
            rad = math.radians(min(360, int(((frame_idx - 11) / 12.0) * 360)))
            nx = flower_center_x + int(65 * math.cos(rad))
            ny = flower_center_y + int(65 * math.sin(rad))
            status_text = "PUNCHING: STITCHING MOTIF EMBROIDERY"
            status_col = C_GOLD
        elif frame_idx <= 27:
            nx = flower_center_x + 70
            ny = 240
            status_text = "LOCK: TIE-OFF END LOCK (૪ ટાંકા પેક)"
            status_col = C_RED
        elif frame_idx <= 30:
            nx = flower_center_x + 70
            ny = 240
            status_text = "TRIM: CUTTING THREAD (કાતર ચાલુ)"
            status_col = C_GOLD
        else:
            ret_progress = (frame_idx - 30) / 5.0
            nx = flower_center_x + 70 - int(ret_progress * (flower_center_x + 70 - origin_x))
            ny = 240
            status_text = "RETURN: PARKING AT MACHINE ORIGIN DR 250 (0,0)"
            status_col = C_BLUE
            
        draw.polygon([(nx, ny), (nx - 7, ny - 22), (nx + 7, ny - 22)], fill=(100, 116, 139))
        draw.line([(nx, ny - 22), (nx, ny - 45)], fill=(71, 85, 105), width=3)
        draw.ellipse([(nx - 4, ny - 4), (nx + 4, ny + 4)], fill=C_GOLD)
        
        draw.rectangle([(0, h - 45), (w, h)], fill=C_DARK)
        draw.text((20, h - 32), f"STATUS: {status_text}", font=font_bold, fill=status_col)
        draw.text((550, h - 32), "Ctrl + Home -> DR 250 Lock", font=font_bold, fill=C_WHITE)
        
        frames.append(img)
        
    out_path = os.path.join(ASSET_DIR, 'anim_lock_origin_dr250.gif')
    frames[0].save(out_path, save_all=True, append_images=frames[1:], duration=150, loop=0)
    print(f"Updated: {out_path}")

def main():
    print("Rebuilding refined educational animated GIFs...")
    make_jump_animation()
    make_sequin_animation()
    make_beads_animation()
    make_paghdi_animation()
    make_lock_origin_animation()
    print("All 5 educational animations rebuilt cleanly!")

if __name__ == '__main__':
    main()
