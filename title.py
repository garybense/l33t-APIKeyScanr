import sys

def print_red_gradient(text_block):
    """
    Applies a vertical TrueColor RGB gradient (shades of red)
    line-by-line to the verified graffiti text block.
    """
    lines = text_block.strip("\n").split("\n")
    total_lines = len(lines)
    
    # Gradient colors: Bright Vivid Red at top -> Deep Crimson at bottom
    start_r, start_g, start_b = 255, 30, 30
    end_r, end_g, end_b = 175, 10, 15

    for i, line in enumerate(lines):
        factor = i / (total_lines - 1) if total_lines > 1 else 0.0
        
        # Calculate intermediate color values
        r = int(start_r + (end_r - start_r) * factor)
        g = int(start_g + (end_g - start_g) * factor)
        b = int(start_b + (end_b - start_b) * factor)
        
        ansi_color = f"\033[38;2;{r};{g};{b}m"
        sys.stdout.write(f"{ansi_color}{line}\033[0m\n")
    sys.stdout.flush()

# Perfect heavy graffiti layout mapped explicitly for 'l33t_APIScanr'
raw_banner = """
 ██▓     ▓█████▄▄  ▓█████▄▄   ▄▄▄█████▓           ▄▄▄       ██▓███   ██▓  ██████  ▄████▄   ▄▄▄       ███▄    █  ██▀███  
▓██▒     ▒░░░░▓██▒ ▒░░░░▓██▒ ▒░░░██▒░░          ▒████▄    ▓██░  ██▒▓██▒▒██    ▒ ▒██▀ ▀█  ▒████▄     ██ ▀█   █ ▓██ ▒ ██▒
▒██░          ▄██▒      ▄██▒     ██▒            ▒██  ▀█▄  ▓██░ ██▓▒▒██▒░ ▓██▄   ▒▓█    ▄ ▒██  ▀█▄  ▓██  ▀█ ██▒▓██ ░▄█ ▒
▒██░         ░░██▒     ░░██▒     ██▒            ░██▄▄▄▄██ ▓██▄█▓▒ ▒░██░  ▒   ██▒▒▓▓▄ ▄██▒░██▄▄▄▄██ ▓██▒  ▐▌██▒▒██▀▀█▄  
░██████▒ ▓█████▄▄▒ ▓█████▄▄▒     ██▒     ██████▒ ▓█   ▓██▒▒██▒ ░  ░░██░▒██████▒▒▒ ▓███▀ ░ ▓█   ▓██▒▒██░   ▓██░░██▓ ▒██▒
  ░░░░░░  ▒░░░░░░░  ▒░░░░░░░      ░░       ░░░░░  ▒▒   ▓▒█░▒▓▒░ ░  ░░▓  ▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒ ░ ▒▓ ░▒▓░
    ░░    ░   ░     ░   ░         ░               ░   ▒   ░░       ▒ ░ ░  ░  ░     ░   ░  ░  ░    ░   ▒      ░   ░ ░   ░░   ░ 
                                                      ░            ░                   ░          ░  ░         ░    ░     
"""

if __name__ == "__main__":
    print_red_gradient(raw_banner)

