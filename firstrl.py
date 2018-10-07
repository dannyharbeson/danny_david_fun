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


class Object:
    #this is a generic object: the player, a monster, an item, the stairs...
    #it's always represented by a character on screen.
    def __init__(self, x, y, char, color):
        self.x = x
        self.y = y
        self.char = char
        self.color = color
 
    def move(self, dx, dy):
        #move by the given amount
        self.x += dx
        self.y += dy
 
    def draw(self):
        #set the color and then draw the character that represents this object at its position
        tcod.console_set_default_foreground(con, self.color)
        tcod.console_put_char(con, self.x, self.y, self.char, tcod.BKGND_NONE)
 
    def clear(self):
        #erase the character that represents this object
        tcod.console_put_char(con, self.x, self.y, ' ', tcod.BKGND_NONE)

player = Object(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, '@', tcod.white)
npc = Object(SCREEN_WIDTH // 2 - 5, SCREEN_HEIGHT // 2, '@', tcod.yellow)
objects = [npc, player]

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
#        player_y -= 1
        player.move(0, -1)
 
    elif tcod.console_is_key_pressed(tcod.KEY_DOWN):
#        player_y += 1
        player.move(0, +1)

    elif tcod.console_is_key_pressed(tcod.KEY_LEFT):
#        player_x -= 1
         player.move(-1, 0)

    elif tcod.console_is_key_pressed(tcod.KEY_RIGHT):
#        player_x += 1
        player.move(+1, 0)




#############################################
# Main Game Loop
#############################################

def main():
    intialize_game()

    exit_game = False
    while not tcod.console_is_window_closed() and not exit_game:
        tcod.console_set_default_foreground(con, tcod.white)

#        tcod.console_put_char(con, player_x, player_y, '@', tcod.BKGND_NONE)

        for object in objects:
            object.draw()

        tcod.console_blit(con, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0, 0)
        tcod.console_flush()

        for object in objects:
            object.clear()
#        tcod.console_put_char(con, player_x, player_y, ' ', tcod.BKGND_NONE)
        
        exit_game = handle_keys()
    
main()
