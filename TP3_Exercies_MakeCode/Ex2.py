def on_forever():
    if input.button_is_pressed(Button.A):
        basic.show_leds("""
                        # . . . .
                        . # . . .
                        . . # . .
                        . . . # .
                        . . . . #
        """)
    if input.button_is_pressed(Button.B):
        basic.show_leds("""
                        . . . . #
                        . . . # .
                        . . # . .
                        . # . . .
                        # . . . .
        """)



def on_forever2():
    if input.logo_is_pressed():
        basic.show_leds("""
                                # . . . #
                                . # . # .
                                . . # . .
                                . # . # .
                                # . . . #
                """)
    else:
        basic.clear_screen()

basic.forever(on_forever)
basic.forever(on_forever2)
