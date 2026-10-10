#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build all 8 Ultra-Realistic Educational Animations for EmCAD:
1. anim_looping_chain_stitch.gif (Brand New: Looping / Chenille / Moss Stitch mechanism)
2. anim_sequin_overlap_lock.gif (Upgraded: 3D metallic sequins with 40% overlap & Fix 26 triangle lock)
3. anim_sequin_double_stack.gif (Brand New: Dual-feeder 5mm gold + 3mm silver stacked sequin)
4. anim_beads_taka_placement.gif (Upgraded: 3D pearl spheres + cutdana glass tubes with taka spacing & 9° tilt)
5. anim_beads_curved_contour.gif (Brand New: Curved contour beads with continuous 9° rotation)
6. anim_jump_stitching_simulation.gif (Upgraded: Realistic needle, presser foot, auto-trim, and jump line)
7. anim_paghdi_column_stitching.gif (Upgraded: F4 column symmetry satin fill)
8. anim_lock_origin_dr250.gif (Upgraded: Start Tie-in, motif, End Tie-off, and DR 250 parking)
"""

import os
import math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

WORKSPACE = '/Users/manavramani/Desktop/emCad_explain_software'
ASSET_DIR = os.path.join(WORKSPACE, 'emCad_organized_assets')
FONT_PATH = '/Library/Fonts/Arial Unicode.ttf'

def get_font(size):
    try:
        return ImageFont.truetype(FONT_PATH, size)
    except:
        return ImageFont.load_default()

C_DARK = (15, 23, 42)
C_NAVY = (15, 41, 74)
C_WHITE = (255, 255, 255)
C_GRID = (226, 232, 240)
C_GOLD = (217, 119, 6)
C_GOLD_LIGHT = (254, 240, 138)
C_RED = (220, 38, 38)
C_GREEN = (5, 150, 105)
C_BLUE = (37, 99, 235)
C_PURPLE = (147, 51, 234)
C_CYAN = (8, 145, 178)
C_MUTED = (100, 116, 139)
C_LIGHT_BG = (248, 250, 252)

# Helper to draw top banner
def draw_banner(draw, w, title_gu, subtitle_en):
    draw.rectangle([(0, 0), (w, 52)], fill=C_NAVY)
    draw.rectangle([(0, 50), (w, 52)], fill=C_GOLD)
    draw.text((20, 8), title_gu, font=get_font(18), fill=C_WHITE)
    draw.text((20, 30), subtitle_en, font=get_font(12), fill=(203, 213, 225))

# Helper to draw HUD Card at bottom
def draw_hud(draw, w, h, items):
    draw.rectangle([(0, h - 56), (w, h)], fill=(10, 25, 47))
    draw.rectangle([(0, h - 56), (w, h - 54)], fill=(37, 99, 235))
    col_w = w / float(len(items))
    for idx, (label, val, color) in enumerate(items):
        x1 = int(idx * col_w) + 6
        x2 = int((idx + 1) * col_w) - 6
        draw.rounded_rectangle([(x1, h - 50), (x2, h - 8)], radius=6, fill=(30, 41, 59))
        draw.text((x1 + 8, h - 44), label, font=get_font(10), fill=(148, 163, 184))
        draw.text((x1 + 8, h - 26), val[:24], font=get_font(11), fill=color)

# ------------------------------------------------------------------------------
# 1. LOOPING / CHENILLE ANIMATION (NEW)
# ------------------------------------------------------------------------------
def make_looping_animation():
    print("Generating anim_looping_chain_stitch.gif...")
    w, h = 800, 480
    frames = []
    total_steps = 40
    
    for f in range(total_steps):
        img = Image.new('RGB', (w, h), (245, 247, 250))
        draw = ImageDraw.Draw(img)
        
        # Grid
        for x in range(0, w, 40): draw.line([(x, 52), (x, h - 56)], fill=C_GRID, width=1)
        for y in range(52, h - 56, 40): draw.line([(0, y), (w, y)], fill=C_GRID, width=1)
        
        draw_banner(draw, w, "EmCAD લૂપિંગ એમ્બ્રોઇડરી સિમ્યુલેશન (Chenille / Terry Loop Mechanics)", 
                    "Hollow Needle Down + Looper Hook 360° + 3D Plush Loop Formation (Loop Height: 3.0mm)")
        
        # Fabric base line
        fabric_y = 280
        draw.rectangle([(0, fabric_y), (w, fabric_y + 12)], fill=(30, 41, 59)) # fabric cross-section
        draw.text((20, fabric_y + 16), "કાપડની સપાટી (Fabric Surface - Navy Velvet)", font=get_font(12), fill=C_NAVY)
        draw.text((20, fabric_y - 20), "ઉપરની બાજુ: 3D લૂપ કાર્પેટ (Upright Plush Loops)", font=get_font(12), fill=C_PURPLE)
        draw.text((580, fabric_y + 16), "નીચેની બાજુ: લૂપર હૂક (Looper Hook)", font=get_font(12), fill=C_MUTED)
        
        # Existing placed loops
        num_loops = min(10, int(f / 3))
        for i in range(num_loops):
            lx = 80 + i * 55
            # Draw 3D plush loop above fabric
            draw.ellipse([(lx - 16, fabric_y - 65), (lx + 16, fabric_y + 2)], fill=(254, 240, 138), outline=C_GOLD, width=3)
            draw.ellipse([(lx - 8, fabric_y - 50), (lx + 8, fabric_y - 10)], fill=(245, 247, 250), outline=C_GOLD, width=2)
            # Needle entry hole on fabric
            draw.ellipse([(lx - 3, fabric_y - 2), (lx + 3, fabric_y + 4)], fill=C_RED)
            draw.text((lx - 8, fabric_y - 85), f"L{i+1}", font=get_font(11), fill=C_GOLD)
            
        # Active needle and current loop formation
        active_x = 80 + num_loops * 55
        cycle_phase = (f % 3) / 3.0 # 0: Needle descending, 0.33: Looper catching, 0.66: Needle retracting
        
        needle_depth = 0
        if cycle_phase < 0.5:
            # Going down
            needle_depth = int(cycle_phase * 2 * 70)
        else:
            # Going up
            needle_depth = int((1.0 - cycle_phase) * 2 * 70)
            
        needle_tip_y = fabric_y - 70 + needle_depth
        
        # Draw Hollow Chenille Needle
        draw.rectangle([(active_x - 4, needle_tip_y - 120), (active_x + 4, needle_tip_y)], fill=(148, 163, 184), outline=C_DARK, width=2)
        # Needle point
        draw.polygon([(active_x - 4, needle_tip_y), (active_x + 4, needle_tip_y), (active_x, needle_tip_y + 16)], fill=(203, 213, 225), outline=C_DARK)
        # Hollow eye showing wool thread inside
        draw.line([(active_x, needle_tip_y - 120), (active_x, needle_tip_y + 10)], fill=C_GOLD, width=3)
        
        # Rotating Looper Hook beneath fabric
        hook_angle = f * 0.4
        hx = active_x + math.cos(hook_angle) * 22
        hy = fabric_y + 40 + math.sin(hook_angle) * 12
        draw.line([(active_x, fabric_y + 20), (hx, hy)], fill=C_PURPLE, width=4)
        draw.ellipse([(hx - 4, hy - 4), (hx + 4, hy + 4)], fill=C_RED)
        
        # Thread loop being formed
        if needle_depth > 30:
            draw.arc([(active_x - 14, fabric_y - 45), (active_x + 14, fabric_y + 10)], 0, 180, fill=C_GOLD, width=3)
            
        # Label active needle
        draw.rectangle([(active_x + 15, needle_tip_y - 60), (active_x + 150, needle_tip_y - 25)], fill=C_WHITE, outline=C_PURPLE, width=2)
        draw.text((active_x + 22, needle_tip_y - 55), "Hollow Needle 120/19", font=get_font(11), fill=C_NAVY)
        draw.text((active_x + 22, needle_tip_y - 40), "Fluffy Wool Thread", font=get_font(11), fill=C_GOLD)
        
        # HUD items
        rpm_val = "520 RPM (Controlled)"
        hud_items = [
            ("MECHANISM", "CHENILLE / TERRY LOOP", C_GOLD),
            ("NEEDLE DEPTH", f"{needle_depth} mm (Stroke)", C_CYAN),
            ("LOOP HEIGHT", "3.00 mm (Plush Velvet)", C_PURPLE),
            ("LOOPER STATUS", "360° SYNCHRONIZED", C_GREEN),
            ("SPEED (RPM)", rpm_val, C_WHITE)
        ]
        draw_hud(draw, w, h, hud_items)
        frames.append(img)
        
    out_path = os.path.join(ASSET_DIR, 'anim_looping_chain_stitch.gif')
    frames[0].save(out_path, save_all=True, append_images=frames[1:], duration=120, loop=0)
    print("Saved:", out_path)

# ------------------------------------------------------------------------------
# 2. SEQUIN OVERLAP & FIX TYPE 26 (UPGRADED)
# ------------------------------------------------------------------------------
def make_sequin_animation():
    print("Generating anim_sequin_overlap_lock.gif...")
    w, h = 800, 480
    frames = []
    total_steps = 42
    
    for f in range(total_steps):
        img = Image.new('RGB', (w, h), (248, 250, 252))
        draw = ImageDraw.Draw(img)
        
        for x in range(0, w, 40): draw.line([(x, 52), (x, h - 56)], fill=C_GRID, width=1)
        for y in range(52, h - 56, 40): draw.line([(0, y), (w, y)], fill=C_GRID, width=1)
        
        draw_banner(draw, w, "EmCAD સિક્વિન (ટિકી) ફીડર ડ્રોપ & Fix Type 26 ત્રિકોણ લૉક સિમ્યુલેશન", 
                    "Feeder Chute Drop + 40% Fish-Scale Overlap + 3-Needle Triangle Lock (120° Spacing)")
        
        # Fabric base line
        draw.line([(40, 260), (760, 260)], fill=(203, 213, 225), width=2)
        
        num_sequins = min(8, int(f / 4))
        for i in range(num_sequins):
            cx = 100 + i * 70
            cy = 230
            # 3D Metallic sequin disc with rim & radial reflection
            draw.ellipse([(cx - 36, cy - 36), (cx + 36, cy + 36)], fill=(245, 158, 11), outline=(180, 83, 9), width=2)
            draw.ellipse([(cx - 32, cy - 32), (cx + 32, cy + 32)], fill=C_GOLD_LIGHT)
            # Specular arc
            draw.arc([(cx - 28, cy - 28), (cx + 28, cy + 28)], 200, 310, fill=C_WHITE, width=4)
            # Center hole
            draw.ellipse([(cx - 6, cy - 6), (cx + 6, cy + 6)], fill=C_DARK, outline=(180, 83, 9), width=1)
            
            # Fix Type 26 triangle stitches (120 deg)
            for ang in [math.pi/2, math.pi * 7/6, math.pi * 11/6]:
                tx = cx + math.cos(ang) * 26
                ty = cy + math.sin(ang) * 26
                draw.line([(cx, cy), (tx, ty)], fill=C_RED, width=3)
                draw.ellipse([(tx - 2, ty - 2), (tx + 2, ty + 2)], fill=C_DARK)
                
            draw.text((cx - 10, cy + 42), f"S{i+1}", font=get_font(12), fill=C_NAVY)
            
        # Current active sequin being dropped and locked
        active_cx = 100 + num_sequins * 70
        active_cy = 230
        step_in_seq = f % 4
        
        # Draw Feeder Chute arm extending from top-right
        feeder_x = active_cx + 40
        feeder_y = 120
        draw.polygon([(feeder_x, feeder_y), (feeder_x + 80, feeder_y - 40), (feeder_x + 95, feeder_y - 25), (feeder_x + 15, feeder_y + 15)], fill=(100, 116, 139), outline=C_DARK)
        draw.text((feeder_x + 30, feeder_y - 45), "Sequin Chute (3mm Feeder)", font=get_font(11), fill=C_NAVY)
        
        if step_in_seq == 0:
            # Dropping
            drop_y = 150
            draw.ellipse([(active_cx - 30, drop_y - 15), (active_cx + 30, drop_y + 15)], fill=C_GOLD_LIGHT, outline=C_GOLD, width=2)
            draw.text((active_cx - 40, drop_y - 35), "1. Feeder Drop", font=get_font(12), fill=C_GOLD)
        elif step_in_seq == 1:
            # Placed on fabric, needle going into center hole
            draw.ellipse([(active_cx - 36, active_cy - 36), (active_cx + 36, active_cy + 36)], fill=C_GOLD_LIGHT, outline=C_GOLD, width=2)
            draw.ellipse([(active_cx - 6, active_cy - 6), (active_cx + 6, active_cy + 6)], fill=C_DARK)
            # Needle penetrating
            draw.rectangle([(active_cx - 3, 110), (active_cx + 3, active_cy)], fill=(203, 213, 225), outline=C_DARK)
            draw.polygon([(active_cx - 3, active_cy), (active_cx + 3, active_cy), (active_cx, active_cy + 10)], fill=(148, 163, 184))
            draw.text((active_cx + 12, 160), "2. Needle Center Strike", font=get_font(12), fill=C_RED)
        else:
            # Stitching Fix 26 triangle legs
            draw.ellipse([(active_cx - 36, active_cy - 36), (active_cx + 36, active_cy + 36)], fill=C_GOLD_LIGHT, outline=C_GOLD, width=2)
            draw.ellipse([(active_cx - 6, active_cy - 6), (active_cx + 6, active_cy + 6)], fill=C_DARK)
            # Triangle stitches
            draw.line([(active_cx, active_cy), (active_cx, active_cy + 26)], fill=C_RED, width=3)
            if step_in_seq >= 2:
                tx = active_cx + math.cos(math.pi * 7/6) * 26
                ty = active_cy + math.sin(math.pi * 7/6) * 26
                draw.line([(active_cx, active_cy), (tx, ty)], fill=C_RED, width=3)
            draw.text((active_cx + 12, 160), "3. Fix 26 Triangle Lock", font=get_font(12), fill=C_GREEN)
            
        hud_items = [
            ("DISC DIAMETER", "3.00 mm (Flat Gold)", C_GOLD),
            ("OVERLAP RATIO", "40% (Fish-Scale)", C_CYAN),
            ("LOCK TYPE", "FIX TYPE 26 (3 Stitches)", C_RED),
            ("STITCH ANGLE", "120° TRI-RADIAL", C_GREEN),
            ("PLACED COUNT", f"{num_sequins} / 8 DISCS", C_WHITE)
        ]
        draw_hud(draw, w, h, hud_items)
        frames.append(img)
        
    out_path = os.path.join(ASSET_DIR, 'anim_sequin_overlap_lock.gif')
    frames[0].save(out_path, save_all=True, append_images=frames[1:], duration=140, loop=0)
    print("Saved:", out_path)

# ------------------------------------------------------------------------------
# 3. DOUBLE SEQUIN STACK ANIMATION (NEW)
# ------------------------------------------------------------------------------
def make_sequin_double_stack_animation():
    print("Generating anim_sequin_double_stack.gif...")
    w, h = 800, 480
    frames = []
    total_steps = 36
    
    for f in range(total_steps):
        img = Image.new('RGB', (w, h), (248, 250, 252))
        draw = ImageDraw.Draw(img)
        
        for x in range(0, w, 40): draw.line([(x, 52), (x, h - 56)], fill=C_GRID, width=1)
        for y in range(52, h - 56, 40): draw.line([(0, y), (w, y)], fill=C_GRID, width=1)
        
        draw_banner(draw, w, "EmCAD ડબલ સિક્વિન સ્ટેકિંગ સિમ્યુલેશન (Dual Stacked Sequin)", 
                    "Device A (5mm Gold Base) + Device B (3mm Hologram Top) + Single Concentric Lock")
        
        num_stacks = min(6, int(f / 5))
        for i in range(num_stacks):
            cx = 120 + i * 95
            cy = 230
            # 5mm Base Sequin
            draw.ellipse([(cx - 44, cy - 44), (cx + 44, cy + 44)], fill=(245, 158, 11), outline=(180, 83, 9), width=2)
            draw.ellipse([(cx - 40, cy - 40), (cx + 40, cy + 40)], fill=C_GOLD_LIGHT)
            # 3mm Top Sequin (Silver Hologram)
            draw.ellipse([(cx - 26, cy - 26), (cx + 26, cy + 26)], fill=(224, 231, 255), outline=C_BLUE, width=2)
            draw.ellipse([(cx - 22, cy - 22), (cx + 22, cy + 22)], fill=(241, 245, 249))
            draw.arc([(cx - 20, cy - 20), (cx + 20, cy + 20)], 180, 320, fill=C_WHITE, width=3)
            # Center hole
            draw.ellipse([(cx - 6, cy - 6), (cx + 6, cy + 6)], fill=C_DARK)
            # 4-point star lock
            for a in [0, math.pi/2, math.pi, math.pi*3/2]:
                draw.line([(cx, cy), (cx + math.cos(a)*18, cy + math.sin(a)*18)], fill=C_RED, width=3)
            draw.text((cx - 15, cy + 50), f"Stack {i+1}", font=get_font(11), fill=C_NAVY)
            
        # Active stack animation
        active_cx = 120 + num_stacks * 95
        active_cy = 230
        phase = f % 5
        
        # Dual Chute Graphic
        draw.rectangle([(active_cx - 60, 90), (active_cx - 10, 150)], fill=(245, 158, 11), outline=C_DARK, width=2)
        draw.text((active_cx - 55, 95), "Chute A\n(5mm)", font=get_font(11), fill=C_WHITE)
        draw.rectangle([(active_cx + 10, 90), (active_cx + 60, 150)], fill=C_BLUE, outline=C_DARK, width=2)
        draw.text((active_cx + 15, 95), "Chute B\n(3mm)", font=get_font(11), fill=C_WHITE)
        
        if phase == 0:
            # Chute A drops 5mm
            draw.ellipse([(active_cx - 40, 180), (active_cx + 40, 205)], fill=C_GOLD_LIGHT, outline=C_GOLD, width=2)
            draw.text((active_cx - 50, 160), "1. Drop 5mm Base", font=get_font(11), fill=C_GOLD)
        elif phase == 1:
            # 5mm on cloth, 3mm falling
            draw.ellipse([(active_cx - 44, active_cy - 44), (active_cx + 44, active_cy + 44)], fill=C_GOLD_LIGHT, outline=C_GOLD, width=2)
            draw.ellipse([(active_cx - 24, 180), (active_cx + 24, 200)], fill=(224, 231, 255), outline=C_BLUE, width=2)
            draw.text((active_cx - 50, 160), "2. Drop 3mm Top", font=get_font(11), fill=C_BLUE)
        elif phase >= 2:
            # Both stacked, needle piercing both
            draw.ellipse([(active_cx - 44, active_cy - 44), (active_cx + 44, active_cy + 44)], fill=C_GOLD_LIGHT, outline=C_GOLD, width=2)
            draw.ellipse([(active_cx - 26, active_cy - 26), (active_cx + 26, active_cy + 26)], fill=(224, 231, 255), outline=C_BLUE, width=2)
            draw.ellipse([(active_cx - 6, active_cy - 6), (active_cx + 6, active_cy + 6)], fill=C_DARK)
            # Needle
            draw.rectangle([(active_cx - 3, 110), (active_cx + 3, active_cy)], fill=(203, 213, 225), outline=C_DARK)
            draw.polygon([(active_cx - 3, active_cy), (active_cx + 3, active_cy), (active_cx, active_cy + 10)], fill=(148, 163, 184))
            draw.text((active_cx + 15, 160), "3. Single Needle Lock", font=get_font(12), fill=C_RED)
            
        hud_items = [
            ("DEVICE A", "5.0 mm FLAT GOLD", C_GOLD),
            ("DEVICE B", "3.0 mm HOLOGRAM SILVER", C_CYAN),
            ("ALIGNMENT", "CONCENTRIC CENTER", C_GREEN),
            ("LOCKING", "SINGLE STRIKE STAR LOCK", C_RED),
            ("APPLICATION", "HAUTE COUTURE BRIDAL", C_WHITE)
        ]
        draw_hud(draw, w, h, hud_items)
        frames.append(img)
        
    out_path = os.path.join(ASSET_DIR, 'anim_sequin_double_stack.gif')
    frames[0].save(out_path, save_all=True, append_images=frames[1:], duration=140, loop=0)
    print("Saved:", out_path)

# ------------------------------------------------------------------------------
# 4. BEADS TAKA PLACEMENT (UPGRADED)
# ------------------------------------------------------------------------------
def make_beads_animation():
    print("Generating anim_beads_taka_placement.gif...")
    w, h = 800, 480
    frames = []
    total_steps = 40
    
    for f in range(total_steps):
        img = Image.new('RGB', (w, h), (248, 250, 252))
        draw = ImageDraw.Draw(img)
        
        for x in range(0, w, 40): draw.line([(x, 52), (x, h - 56)], fill=C_GRID, width=1)
        for y in range(52, h - 56, 40): draw.line([(0, y), (w, y)], fill=C_GRID, width=1)
        
        draw_banner(draw, w, "EmCAD બીડ્સ (મોતી & કટદાણા) ટાંકો લંબાઈ અને ૯° ટિલ્ટ સિમ્યુલેશન", 
                    "Round Pearl Taka: 2.30mm | Cutdana Bugle Tube: 4.50mm | Alt+CapsLock: 9° Needle Tilt")
        
        # Track 1: Round Pearls
        draw.text((40, 75), "ટ્રેક ૧: ગોળ મોતી (Round Pearl - Diameter: 2.0mm, Taka: 2.30mm)", font=get_font(13), fill=C_NAVY)
        draw.line([(40, 140), (760, 140)], fill=(203, 213, 225), width=2)
        
        num_pearls = min(8, int(f / 3))
        for i in range(num_pearls):
            px = 80 + i * 75
            py = 140
            # 3D pearl sphere with soft shading & specular
            draw.ellipse([(px - 20, py - 20), (px + 20, py + 20)], fill=(241, 245, 249), outline=(148, 163, 184), width=2)
            draw.ellipse([(px - 14, py - 14), (px + 14, py + 14)], fill=(255, 255, 255))
            draw.ellipse([(px - 8, py - 10), (px - 2, py - 4)], fill=C_WHITE) # highlight
            # Thread through hole
            draw.line([(px - 26, py), (px + 26, py)], fill=C_RED, width=3)
            draw.ellipse([(px - 26, py - 2), (px - 22, py + 2)], fill=C_DARK)
            draw.ellipse([(px + 22, py - 2), (px + 26, py + 2)], fill=C_DARK)
            # Taka ruler
            if i == 1:
                draw.line([(px - 26, py + 26), (px + 26, py + 26)], fill=C_BLUE, width=2)
                draw.text((px - 22, py + 30), "2.30 mm", font=get_font(11), fill=C_BLUE)
                
        # Track 2: Cutdana Glass Pipes
        draw.text((40, 235), "ટ્રેક ૨: કટદાણા કાચની નળી (Cutdana Bugle - Length: 4.0mm, Taka: 4.50mm, 9° Tilt)", font=get_font(13), fill=C_NAVY)
        draw.line([(40, 310), (760, 310)], fill=(203, 213, 225), width=2)
        
        num_pipes = min(5, int(f / 5))
        for i in range(num_pipes):
            bx = 100 + i * 115
            by = 310
            # Alt+CapsLock tilt of 9 degrees
            tilt = math.radians(9 * (i % 3))
            # Glass tube cylinder
            draw.rectangle([(bx - 36, by - 12), (bx + 36, by + 12)], fill=C_GOLD_LIGHT, outline=C_GOLD, width=2)
            draw.line([(bx - 36, by - 4), (bx + 36, by - 4)], fill=C_WHITE, width=2)
            # Thread
            draw.line([(bx - 45, by), (bx + 45, by)], fill=C_RED, width=3)
            draw.ellipse([(bx - 45, by - 2), (bx - 41, by + 2)], fill=C_DARK)
            draw.ellipse([(bx + 41, by - 2), (bx + 45, by + 2)], fill=C_DARK)
            if i == 0:
                draw.line([(bx - 45, by + 18), (bx + 45, by + 18)], fill=C_GOLD, width=2)
                draw.text((bx - 20, by + 22), "4.50 mm", font=get_font(11), fill=C_GOLD)
                
        # Needle indicator
        active_x = 100 + num_pipes * 115
        draw.polygon([(active_x - 4, 260), (active_x + 4, 260), (active_x, 305)], fill=(148, 163, 184), outline=C_DARK)
        draw.text((active_x + 8, 270), "Needle (9° Step Tilt)", font=get_font(11), fill=C_RED)
        
        hud_items = [
            ("PEARL TAKA", "2.30 mm (Diameter + 0.3mm)", C_CYAN),
            ("CUTDANA TAKA", "4.50 mm (Length + 0.5mm)", C_GOLD),
            ("NEEDLE ROTATION", "Alt + CapsLock: 9° STEP", C_RED),
            ("GLASS PROTECTION", "PREVENTS TUBE CRACKING", C_GREEN),
            ("SPEED (RPM)", "650 RPM STABLE", C_WHITE)
        ]
        draw_hud(draw, w, h, hud_items)
        frames.append(img)
        
    out_path = os.path.join(ASSET_DIR, 'anim_beads_taka_placement.gif')
    frames[0].save(out_path, save_all=True, append_images=frames[1:], duration=130, loop=0)
    print("Saved:", out_path)

# ------------------------------------------------------------------------------
# 5. BEADS CURVED CONTOUR ANIMATION (NEW)
# ------------------------------------------------------------------------------
def make_beads_curved_animation():
    print("Generating anim_beads_curved_contour.gif...")
    w, h = 800, 480
    frames = []
    total_steps = 38
    
    for f in range(total_steps):
        img = Image.new('RGB', (w, h), (248, 250, 252))
        draw = ImageDraw.Draw(img)
        
        for x in range(0, w, 40): draw.line([(x, 52), (x, h - 56)], fill=C_GRID, width=1)
        for y in range(52, h - 56, 40): draw.line([(0, y), (w, y)], fill=C_GRID, width=1)
        
        draw_banner(draw, w, "EmCAD વળાંકવાળા પાથ પર બીડ્સ & કટદાણા ૯° ટિલ્ટ સિમ્યુલેશન", 
                    "Continuous S-Curve Neckline Contour + Real-Time Tangent Alignment (Alt+CapsLock)")
        
        # Curve formula: y = 240 + sin(x/80) * 80
        curve_pts = []
        for cx in range(60, 740, 5):
            cy = int(240 + math.sin(cx / 70.0) * 80)
            curve_pts.append((cx, cy))
        draw.line(curve_pts, fill=(203, 213, 225), width=2)
        
        num_items = min(12, int(f / 2.5))
        for i in range(num_items):
            t_x = 80 + i * 50
            t_y = int(240 + math.sin(t_x / 70.0) * 80)
            # Tangent angle
            slope = math.cos(t_x / 70.0) * (80.0 / 70.0)
            ang = math.atan(slope)
            # Round to nearest 9 degrees
            ang_deg = round(math.degrees(ang) / 9.0) * 9
            ang_rad = math.radians(ang_deg)
            
            if i % 2 == 0:
                # Pearl
                draw.ellipse([(t_x - 14, t_y - 14), (t_x + 14, t_y + 14)], fill=(241, 245, 249), outline=C_BLUE, width=2)
                draw.ellipse([(t_x - 4, t_y - 4), (t_x + 4, t_y + 4)], fill=C_WHITE)
            else:
                # Cutdana
                dx = math.cos(ang_rad) * 18
                dy = math.sin(ang_rad) * 18
                draw.line([(t_x - dx, t_y - dy), (t_x + dx, t_y + dy)], fill=C_GOLD, width=10)
                draw.line([(t_x - dx, t_y - dy), (t_x + dx, t_y + dy)], fill=C_GOLD_LIGHT, width=4)
                
            draw.ellipse([(t_x - 3, t_y - 3), (t_x + 3, t_y + 3)], fill=C_RED)
            
        # Active needle head rotating
        active_x = 80 + num_items * 50
        active_y = int(240 + math.sin(active_x / 70.0) * 80)
        active_slope = math.cos(active_x / 70.0) * (80.0 / 70.0)
        active_deg = round(math.degrees(math.atan(active_slope)) / 9.0) * 9
        
        draw.line([(active_x, active_y - 80), (active_x, active_y)], fill=(148, 163, 184), width=4)
        draw.ellipse([(active_x - 5, active_y - 5), (active_x + 5, active_y + 5)], fill=C_RED)
        
        # Angle indicator
        draw.rectangle([(active_x + 10, active_y - 70), (active_x + 160, active_y - 35)], fill=C_WHITE, outline=C_BLUE, width=2)
        draw.text((active_x + 18, active_y - 65), f"Tangent Angle: {active_deg}°", font=get_font(11), fill=C_BLUE)
        draw.text((active_x + 18, active_y - 50), "Alt+CapsLock 9° Step", font=get_font(11), fill=C_RED)
        
        hud_items = [
            ("PATH TYPE", "S-CURVE NECKLINE CONTOUR", C_CYAN),
            ("ROTATION MODE", "ALT + CAPSLOCK (9° STEP)", C_GOLD),
            ("CURRENT TILT", f"{active_deg}° ALIGNED", C_GREEN),
            ("TANGENT SAFETY", "ZERO BEAD COLLISION", C_WHITE),
            ("ELEMENTS", f"{num_items} / 12 PLACED", C_RED)
        ]
        draw_hud(draw, w, h, hud_items)
        frames.append(img)
        
    out_path = os.path.join(ASSET_DIR, 'anim_beads_curved_contour.gif')
    frames[0].save(out_path, save_all=True, append_images=frames[1:], duration=130, loop=0)
    print("Saved:", out_path)

# ------------------------------------------------------------------------------
# 6. JUMP & AUTO-TRIM ANIMATION (UPGRADED)
# ------------------------------------------------------------------------------
def make_jump_animation():
    print("Generating anim_jump_stitching_simulation.gif...")
    w, h = 800, 480
    frames = []
    total_steps = 42
    
    for f in range(total_steps):
        img = Image.new('RGB', (w, h), (248, 250, 252))
        draw = ImageDraw.Draw(img)
        
        for x in range(0, w, 40): draw.line([(x, 52), (x, h - 56)], fill=C_GRID, width=1)
        for y in range(52, h - 56, 40): draw.line([(0, y), (w, y)], fill=C_GRID, width=1)
        
        draw_banner(draw, w, "EmCAD સિમ્યુલેશન: મશીન સ્ટીચિંગ vs જમ્પ (Stitch vs Jump Mechanics)", 
                    "Solid Red Stitches + Auto-Trim Scissors + Dotted Blue Jump Vector (Needle High)")
        
        # Object 1 area
        draw.rounded_rectangle([(60, 140), (280, 320)], radius=8, outline=(148, 163, 184), width=1)
        draw.text((70, 115), "ઓબ્જેક્ટ ૧ (Leaf Motif - Red Thread)", font=get_font(12), fill=C_NAVY)
        
        # Object 2 area
        draw.rounded_rectangle([(500, 140), (720, 320)], radius=8, outline=(148, 163, 184), width=1)
        draw.text((510, 115), "ઓબ્જેક્ટ ૨ (Flower Bud - Green Thread)", font=get_font(12), fill=C_NAVY)
        
        # Draw Object 1 stitches
        max_s1 = min(18, int(f / 1.2))
        for i in range(max_s1):
            sx = 80 + i * 10
            y1 = 170 + (i % 2) * 100
            y2 = y1 + 30
            draw.line([(sx, y1), (sx, y2)], fill=C_RED, width=3)
            if i > 0:
                prev_x = 80 + (i - 1) * 10
                prev_y = 170 + ((i - 1) % 2) * 100 + 30
                draw.line([(prev_x, prev_y), (sx, y1)], fill=C_RED, width=2)
                
        # Status calculation
        status_text = "NEEDLE DOWN: STITCHING LEAF MOTIF"
        needle_x = 80 + max_s1 * 10
        needle_y = 230
        
        # Trim Phase (Frames 22 to 28)
        if f >= 22 and f < 28:
            draw.rectangle([(250, 210), (340, 250)], fill=(254, 243, 199), outline=C_GOLD, width=2)
            draw.text((260, 222), "[TRIM SCISSORS]", font=get_font(11), fill=C_GOLD)
            status_text = "AUTO-TRIM: CUTTING THREAD (કાતર સક્રિય)"
            needle_x = 260
            needle_y = 230
            
        # Jump Phase (Frames 28 to 36)
        elif f >= 28 and f < 36:
            j_prog = (f - 28) / 8.0
            needle_x = 260 + j_prog * 250
            needle_y = 230
            # Dotted jump line
            for jx in range(260, int(needle_x), 12):
                draw.line([(jx, 230), (jx + 6, 230)], fill=C_BLUE, width=3)
            status_text = "JUMP: NEEDLE HIGH (ડોટેડ વાદળી જમ્પ લાઇન)"
            draw.text((340, 190), "JUMP (Frame moving, needle up)", font=get_font(12), fill=C_BLUE)
            
        # Object 2 Stitching (Frames 36 to 42)
        elif f >= 36:
            # Full jump line
            for jx in range(260, 510, 12):
                draw.line([(jx, 230), (jx + 6, 230)], fill=C_BLUE, width=3)
            max_s2 = min(12, int((f - 36) * 2))
            for i in range(max_s2):
                sx = 510 + i * 14
                y1 = 170 + (i % 2) * 100
                y2 = y1 + 30
                draw.line([(sx, y1), (sx, y2)], fill=C_GREEN, width=3)
                if i > 0:
                    prev_x = 510 + (i - 1) * 14
                    prev_y = 170 + ((i - 1) % 2) * 100 + 30
                    draw.line([(prev_x, prev_y), (sx, y1)], fill=C_GREEN, width=2)
            needle_x = 510 + max_s2 * 14
            needle_y = 230
            status_text = "OBJECT 2: GREEN THREAD STITCHING ACTIVE"
            
        # Realistic Needle Bar + Presser Foot Assembly
        draw.rectangle([(needle_x - 3, 90), (needle_x + 3, needle_y)], fill=(148, 163, 184), outline=C_DARK)
        draw.polygon([(needle_x - 3, needle_y), (needle_x + 3, needle_y), (needle_x, needle_y + 12)], fill=(203, 213, 225))
        # Presser foot ring
        draw.ellipse([(needle_x - 12, needle_y - 6), (needle_x + 12, needle_y + 12)], outline=C_GOLD, width=2)
        
        hud_items = [
            ("CURRENT MODE", status_text[:28], C_RED if "STITCH" in status_text else C_CYAN),
            ("NEEDLE Z-AXIS", "HIGH (JUMP)" if "JUMP" in status_text else "DOWN (PIERCING)", C_GOLD),
            ("TRIM COMMAND", "AUTO-CUT >= 5.0mm", C_GREEN),
            ("TENSION DISK", "ENGAGED 110g", C_WHITE),
            ("STITCH COUNT", f"{f * 12} TAKA", C_PURPLE)
        ]
        draw_hud(draw, w, h, hud_items)
        frames.append(img)
        
    out_path = os.path.join(ASSET_DIR, 'anim_jump_stitching_simulation.gif')
    frames[0].save(out_path, save_all=True, append_images=frames[1:], duration=130, loop=0)
    print("Saved:", out_path)

# ------------------------------------------------------------------------------
# 7. PAGHDI COLUMN SYMMETRY (UPGRADED)
# ------------------------------------------------------------------------------
def make_paghdi_animation():
    print("Generating anim_paghdi_column_stitching.gif...")
    w, h = 800, 480
    frames = []
    total_steps = 38
    
    for f in range(total_steps):
        img = Image.new('RGB', (w, h), (248, 250, 252))
        draw = ImageDraw.Draw(img)
        
        for x in range(0, w, 40): draw.line([(x, 52), (x, h - 56)], fill=C_GRID, width=1)
        for y in range(52, h - 56, 40): draw.line([(0, y), (w, y)], fill=C_GRID, width=1)
        
        draw_banner(draw, w, "EmCAD પાઘડી (Paghdi F4) કોલમ સિમેટ્રી સાટિન સ્ટીચિંગ", 
                    "Dual Rail Guides + Angle Lines (15° to 75°) + Smooth Satin Fill Density (Width >= 0.8mm)")
        
        cx = w // 2
        # Centerline
        draw.line([(cx, 80), (cx, 380)], fill=(203, 213, 225), width=2)
        draw.text((cx + 10, 85), "Centerline Axis (X=0)", font=get_font(11), fill=C_MUTED)
        
        # Paghdi rails
        steps_total = 32
        prog = min(1.0, f / 30.0)
        curr_steps = int(prog * steps_total)
        
        # Draw Satin stitches
        for i in range(curr_steps):
            py = 100 + i * 8
            half_w = 40 + math.sin(i * 0.16) * 65
            ang = math.radians(15 + (i / float(steps_total)) * 60)
            dx = math.cos(ang) * half_w
            dy = math.sin(ang) * (half_w * 0.2)
            draw.line([(cx - dx, py - dy), (cx + dx, py + dy)], fill=C_GOLD, width=3)
            draw.ellipse([(cx - dx - 2, py - dy - 2), (cx - dx + 2, py - dy + 2)], fill=C_RED)
            draw.ellipse([(cx + dx - 2, py + dy - 2), (cx + dx + 2, py + dy + 2)], fill=C_RED)
            
        # Draw Left and Right boundary rails
        left_rail = []
        right_rail = []
        for i in range(steps_total):
            py = 100 + i * 8
            half_w = 40 + math.sin(i * 0.16) * 65
            ang = math.radians(15 + (i / float(steps_total)) * 60)
            dx = math.cos(ang) * half_w
            dy = math.sin(ang) * (half_w * 0.2)
            left_rail.append((cx - dx, py - dy))
            right_rail.append((cx + dx, py + dy))
            
        draw.line(left_rail, fill=C_BLUE, width=2)
        draw.line(right_rail, fill=C_BLUE, width=2)
        
        # Rail labels
        draw.text((left_rail[0][0] - 80, left_rail[0][1]), "Rail 1 (F4)", font=get_font(11), fill=C_BLUE)
        draw.text((right_rail[0][0] + 15, right_rail[0][1]), "Rail 2 (F4)", font=get_font(11), fill=C_BLUE)
        
        hud_items = [
            ("TOOL COMMAND", "F4 COLUMN SYMMETRY", C_GOLD),
            ("STITCH TYPE", "SATIN / ZIGZAG DENSITY", C_CYAN),
            ("MINIMUM WIDTH", "0.80 mm (Needle Safe)", C_RED),
            ("ANGLE SWEEP", "15° TO 75° GRADUAL", C_GREEN),
            ("FILL PROGRESS", f"{int(prog * 100)}% COMPLETE", C_WHITE)
        ]
        draw_hud(draw, w, h, hud_items)
        frames.append(img)
        
    out_path = os.path.join(ASSET_DIR, 'anim_paghdi_column_stitching.gif')
    frames[0].save(out_path, save_all=True, append_images=frames[1:], duration=130, loop=0)
    print("Saved:", out_path)

# ------------------------------------------------------------------------------
# 8. ORIGIN LOCK DR 250 (UPGRADED)
# ------------------------------------------------------------------------------
def make_origin_animation():
    print("Generating anim_lock_origin_dr250.gif...")
    w, h = 800, 480
    frames = []
    total_steps = 40
    
    for f in range(total_steps):
        img = Image.new('RGB', (w, h), (248, 250, 252))
        draw = ImageDraw.Draw(img)
        
        for x in range(0, w, 40): draw.line([(x, 52), (x, h - 56)], fill=C_GRID, width=1)
        for y in range(52, h - 56, 40): draw.line([(0, y), (w, y)], fill=C_GRID, width=1)
        
        draw_banner(draw, w, "EmCAD ઓરિજિન લૉક DR 250 & ટાઇ-ઇન / ટાઇ-ઓફ સિમ્યુલેશન", 
                    "Origin Park Point (0,0) -> 3 Tie-In Stitches -> Motif -> 4 Tie-Off Stitches -> Return DR 250")
        
        # Origin DR 250 Base
        ox, oy = 100, 240
        draw.ellipse([(ox - 18, oy - 18), (ox + 18, oy + 18)], outline=C_CYAN, width=3)
        draw.line([(ox - 24, oy), (ox + 24, oy)], fill=C_CYAN, width=2)
        draw.line([(ox, oy - 24), (ox, oy + 24)], fill=C_CYAN, width=2)
        draw.text((ox - 45, oy + 24), "ORIGIN DR 250 (0,0)", font=get_font(11), fill=C_NAVY)
        
        # Motif Frame Area
        mx, my = 440, 140
        mw, mh = 260, 200
        draw.rounded_rectangle([(mx, my), (mx + mw, my + mh)], radius=10, fill=(255, 255, 255), outline=C_BLUE, width=2)
        draw.text((mx + 15, my + 15), "Embroidery Motif Area (Flower Pattern)", font=get_font(12), fill=C_NAVY)
        
        status_lbl = "TRAVELING TO DESIGN START"
        cur_x, cur_y = ox, oy
        
        if f < 10:
            # Traveling from Origin to Motif start
            p = f / 10.0
            cur_x = int(ox + p * (mx + 30 - ox))
            cur_y = int(oy + p * (my + 40 - oy))
            # dashed travel line
            for lx in range(ox, cur_x, 10):
                draw.line([(lx, oy), (lx + 5, oy)], fill=C_CYAN, width=2)
        elif f < 16:
            # 3 Tie-in lock stitches
            cur_x = mx + 30
            cur_y = my + 40
            draw.ellipse([(cur_x - 12, cur_y - 12), (cur_x + 12, cur_y + 12)], fill=(254, 240, 138), outline=C_RED, width=2)
            draw.text((cur_x + 18, cur_y - 10), "3 Tie-In Stitches Lock", font=get_font(11), fill=C_RED)
            status_lbl = "TIE-IN: 3 MICRO LOCK STITCHES (દોરો બાંધવો)"
        elif f < 28:
            # Stitching motif inside area
            cur_x = mx + 30 + int(((f - 16) / 12.0) * 180)
            cur_y = my + 60 + int(math.sin(f * 0.8) * 40)
            # Motif curves
            draw.arc([(mx + 20, my + 40), (mx + 140, my + 160)], 0, 360, fill=C_GOLD, width=3)
            draw.arc([(mx + 120, my + 40), (mx + 240, my + 160)], 0, 360, fill=C_GREEN, width=3)
            status_lbl = "STITCHING MOTIF EMBROIDERY (કામ ચાલુ)"
        elif f < 34:
            # 4 Tie-off stitches + trim
            cur_x = mx + 210
            cur_y = my + 100
            draw.ellipse([(cur_x - 12, cur_y - 12), (cur_x + 12, cur_y + 12)], fill=(254, 240, 138), outline=C_RED, width=2)
            draw.text((cur_x - 130, cur_y - 25), "4 Tie-Off Stitches + Trim", font=get_font(11), fill=C_RED)
            status_lbl = "TIE-OFF: 4 LOCK STITCHES + AUTO-TRIM"
        else:
            # Returning to DR 250
            p = (f - 34) / 6.0
            cur_x = int(mx + 210 - p * (mx + 210 - ox))
            cur_y = int(my + 100 - p * (my + 100 - oy))
            status_lbl = "RETURNING TO DR 250 ORIGIN PARK POSITION"
            
        # Draw needle indicator
        draw.polygon([(cur_x - 4, cur_y - 30), (cur_x + 4, cur_y - 30), (cur_x, cur_y)], fill=C_RED, outline=C_DARK)
        
        hud_items = [
            ("MACHINE STATUS", status_lbl[:28], C_GOLD),
            ("ORIGIN POINT", "DR 250 (0.00, 0.00) mm", C_CYAN),
            ("TIE-IN RULE", "3 REVERSE STITCHES", C_GREEN),
            ("TIE-OFF RULE", "4 MICRO LOCK STITCHES", C_RED),
            ("FRAME REPEAT", "100% PERFECT REGISTRATION", C_WHITE)
        ]
        draw_hud(draw, w, h, hud_items)
        frames.append(img)
        
    out_path = os.path.join(ASSET_DIR, 'anim_lock_origin_dr250.gif')
    frames[0].save(out_path, save_all=True, append_images=frames[1:], duration=140, loop=0)
    print("Saved:", out_path)

def main():
    print("Starting generation of all 8 animation plates...")
    make_looping_animation()
    make_sequin_animation()
    make_sequin_double_stack_animation()
    make_beads_animation()
    make_beads_curved_animation()
    make_jump_animation()
    make_paghdi_animation()
    make_origin_animation()
    print("All 8 animations generated successfully in emCad_organized_assets!")

if __name__ == '__main__':
    main()
