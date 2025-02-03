from ._anvil_designer import FadingTextComponentTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class FadingTextComponent(FadingTextComponentTemplate):
    def __init__(self, **properties):
        # Initialize internal attributes
        self._text = ""
        self._delay = 100
        self._font = "Jura, Ubuntu, Roboto, Noto, Arial, sans-serif"
        self._size = "16px"
        self._bold = False
        self._foreground_color = "black"
        self._background_color = "transparent"
        self._wrap_on_mobile = True
        self._text_align = "left"

        # Initialize components and apply initial styles
        self.init_components(**properties)
        self._apply_styles()

    def _apply_styles(self):
        """Apply font, color, and bold styles to the text container."""
        container = self.dom_nodes['fading-text-container']
        container.style.fontFamily = self._font
        container.style.fontSize = self._size
        container.style.fontWeight = "bold" if self._bold else "normal"
        container.style.color = self._foreground_color
        container.style.backgroundColor = self._background_color
        container.style.textAlign=self._text_align

        # Handle wrapping
        if not self._wrap_on_mobile:
            container.classList.add("no-wrap")
        else:
            container.classList.remove("no-wrap")
    @property
    def text_align(self):
        """Property to get or set the text alignment."""
        return self._text_align

    @text_align.setter
    def text_align(self, value):
        if value in {"left", "center", "right"}:
            self._text_align = value
            self._apply_styles()
        else:
            raise ValueError("text_align must be 'left', 'center', or 'right'")
          
    @property
    def wrap_on_mobile(self):
        """Property to get or set the wrapping behavior on mobile."""
        return self._wrap_on_mobile

    @wrap_on_mobile.setter
    def wrap_on_mobile(self, value):
        self._wrap_on_mobile = value
        self._apply_styles()
      
    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value
        self._render_text()

    @property
    def font(self):
        return self._font

    @font.setter
    def font(self, value):
        self._font = value
        self._apply_styles()

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value
        self._apply_styles()

    @property
    def bold(self):
        return self._bold

    @bold.setter
    def bold(self, value):
        self._bold = value
        self._apply_styles()

    @property
    def foreground_color(self):
        """Property to get or set the text color."""
        return self._foreground_color

    @foreground_color.setter
    def foreground_color(self, value):
        self._foreground_color = value
        self._apply_styles()

    @property
    def background_color(self):
        """Property to get or set the background color."""
        return self._background_color

    @background_color.setter
    def background_color(self, value):
        self._background_color = value
        self._apply_styles()

    def _render_text(self):
        """Handles fading in each character one at a time."""
        container = self.dom_nodes['fading-text-container']
        container.innerHTML = ""  # Clear existing text

        for index, char in enumerate(self._text):
            span = self._create_char_element(char, index * self._delay)
            container.appendChild(span)

    def _create_char_element(self, char, delay):
        """Create a span element for each character with an animation delay."""
        span = anvil.js.window.document.createElement('span')
        span.textContent = char if char != " " else '\u00A0'
        span.className = "fading-char"
        span.style.animationDelay = f"{delay}ms"
        return span

    def fade_in_text(self, text, delay=100):
        """Public method to set text and fade it in with a specified delay."""
        self._delay = delay
        self.text = text
