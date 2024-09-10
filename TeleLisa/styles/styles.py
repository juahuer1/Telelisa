import reflex as rx
from enum import Enum

class Size(Enum):
    XS = "0.8em"
    S = "1em"
    L = "2em"
    XL= "4em"
    XXL="6em"

######## STYLES DESKTOP
## MAIN PAGE
main_page_style = dict(
    max_width="85%",
    align_items="center"
)

# NAVBAR
navbar_style = dict(
    bg=rx.color("accent", 3),
    padding=Size.S,
    position="fixed",
    top="0px",
    z_index="999",
    width="100%",
    heigth=Size.XL
)

navbar_title_style = dict(
    size="7", 
    weight="bold"
)

navbar_image_style = dict(
    width="2.25em",
    height="auto",
    border_radius="25%",
)

# HEADER
header_style = dict(
    margin_top=Size.XL,
    padding = Size.L,
)

avatar_style = dict(
    margin_left = Size.S,
    margin_right = Size.S,  
)

# TV
tv_video_style = dict(
    flex_shrink = "0",  # No se encogerá
    flex_grow = "0",    # No crecerá
)




######## STYLES MOBILE
## NAVBAR

# navbar_title_style = dict(
#     size="6", 
#     weight="bold"
# )

# navbar_image_style = dict(
#     width="2em",
#     height="auto",
#     border_radius="25%",
# )