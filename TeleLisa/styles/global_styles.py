import reflex as rx
from TeleLisa.styles.colors import Colors, TextColors


BASE_STYLES = {
    rx.button: {
        "color": TextColors.BODY.value,
    },
    rx.text: {
        "color": TextColors.BODY.value,
    },
    rx.select: {
        "color" : TextColors.BODY.value,
    },
    rx.link: {
        "color" : Colors.PRIMARY.value
    },
    rx.heading: {
        "color" : TextColors.HEADER.value
    },
    rx.grid: {
        "width" : "100%"
    }
}