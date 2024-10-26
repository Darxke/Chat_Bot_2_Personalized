from streamlit_image_select import image_select
import streamlit as st
def img():
    img = image_select("Label", ["https://media.discordapp.net/attachments/840396747729928214/1299527061848981545/image.jpg?ex=671d8663&is=671c34e3&hm=7ab58ed96c7351c8f346bdaff1b0d139a247b410feb05a2811dbea9ab73b2735&=&format=webp&width=705&height=941",
                                 "https://media.discordapp.net/attachments/840396747729928214/1299528892310224916/image.jpg?ex=671d8818&is=671c3698&hm=5d12bc90c57d93a20e4fc221dd661ca39eeab60bc4247be381f584af37896df3&=&format=webp&width=705&height=939",
                                 "https://media.discordapp.net/attachments/840396747729928214/1299528250686443581/image.jpg?ex=671d877f&is=671c35ff&hm=85edd5038a2c0db2ecf89281d0b66947d5bc7d3f17d00bc1c356558dad1a9fad&=&format=webp&width=705&height=939"])
