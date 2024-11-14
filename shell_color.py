#!/usr/bin/env python3
"""shell_color.py

Description:
    Print text output to terminal in color
"""


def stringc( string , *rgb ):
    """Generate the escape seq. for shell colors"""
    r , g , b = rgb
    return f"\x1b[38;2;{r};{g};{b}m{string}\x1b[0m"

def string_blink( string ):
    """Generate escape sequence for blinking text"""
    return f"\033[5m{string}\033[0m"

def printc( string , *rgb ):
    _string = stringc( string , *rgb )
    print( _string )


if __name__ == '__main__':
    # Color is a tuple of RGB
    # Values are from 0 to 255
    _color = ( 248 , 0 , 131 )
    printc( "This is in color!!!" , *_color )
