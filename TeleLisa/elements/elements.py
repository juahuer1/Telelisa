import reflex as rx
import TeleLisa.styles.styles as styles

def RxGrid(data, columns: str = "3", spacing: str = styles.Size.DEFAULT.value, width: str = "100%", **kwargs) -> rx.Component:
    return rx.grid(
        data,
        columns = columns,
        spacing = spacing,
        width=width,
        **kwargs
    )

def RxLink(data, href: str, is_external: bool = False, **kwargs) -> rx.Component:
    return rx.link(
        data,
        href=href,
        is_external=is_external,
        **kwargs
    )

def RxButton(data, color_scheme: str = "brown", size: str = "3", **kwargs) -> rx.Component:
    return rx.button(
        data,
        color_scheme=color_scheme,
        size=size,
        **kwargs
    )

def RxSelect(data, color_scheme: str = "brown", variant: str = "soft", placeholder: str = "Seleccione...", **kwargs) -> rx.Component:
    return rx.select(
        data,
        color_scheme=color_scheme,
        variant=variant,
        placeholder=placeholder,
        **kwargs
    )

def RxText(data, size: str = styles.TextSizes.DEFAULT.value, **kwargs) -> rx.Component:
    return rx.text(
        data,
        size=size,
        **kwargs
    )