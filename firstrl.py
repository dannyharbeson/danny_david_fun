#C:\Users\Danny\Documents\Projects\first_project
import tcod as tcod

# ######################################################################
# Global Game Settings
# ######################################################################
# Windows Controls
FULLSCREEN = False
SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50
LIMIT_FPS = 20
# Game controls
TURN_BASED = True

# con = tcod.console_new(SCREEN_WIDTH, SCREEN_WIDTH)

def intialize_game():
    # Setup player
    global player_x, player_y, con
    player_x = SCREEN_WIDTH // 2
    player_y = SCREEN_HEIGHT // 2

    # Setup font
    font_path = 'arial10x10.png'  # this will look in the same folder as this script
    font_flags = tcod.FONT_TYPE_GREYSCALE | tcod.FONT_LAYOUT_TCOD  # the layout may need to change with a different font file
    tcod.console_set_custom_font(font_path, font_flags)

    # Initialize screen
    title = "Python 3 + tcod tutorial"
    con = tcod.console_new(SCREEN_WIDTH, SCREEN_WIDTH)
    tcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, title, FULLSCREEN)

    # Set FPS
    tcod.sys_set_fps(LIMIT_FPS)

# ######################################################################
# User Input
# ######################################################################
def get_key_event(turn_based=None):
    if turn_based:
        key = tcod.console_wait_for_keypress(True)
    else:
        key = tcod.console_check_for_keypress()
    return key
    
def handle_keys():
    global player_x, player_y

    key = get_key_event(TURN_BASED)

    if key.vk == tcod.KEY_ENTER and key.lalt:
    # Alt + enter = toggle fullscreen
        tcod.console_set_fullscreen(not tcod.console_is_fullscreen())

    elif key.vk == tcod.KEY_ESCAPE:
        return True  #  Exit game

    # movement keys
    if tcod.console_is_key_pressed(tcod.KEY_UP):
        player_y -= 1
 
    elif tcod.console_is_key_pressed(tcod.KEY_DOWN):
        player_y += 1
 
    elif tcod.console_is_key_pressed(tcod.KEY_LEFT):
        player_x -= 1
 
    elif tcod.console_is_key_pressed(tcod.KEY_RIGHT):
        player_x += 1

#############################################
# Main Game Loop
#############################################

def main():
    intialize_game()

    exit_game = False
    while not tcod.console_is_window_closed() and not exit_game:
        tcod.console_set_default_foreground(con, tcod.white)
        tcod.console_put_char(con, player_x, player_y, '@', tcod.BKGND_NONE)
        tcod.console_blit(con, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0, 0)
        tcod.console_flush()
        tcod.console_put_char(con, player_x, player_y, ' ', tcod.BKGND_NONE)
        
        exit_game = handle_keys()
    
main()