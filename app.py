import streamlit as st
import random

st.title("🍽 今日のお店を決めよう！")

cuisine = st.radio("ジャンルを選んでください", ["居酒屋", "洋食屋", "カフェ"])

restaurants = {
    "居酒屋": ["海鮮居酒屋 天秤棒", "居酒屋大御所", "大衆酒場 タムヤ"],
    "洋食屋": ["トロイカ＆リビエラ", "Cafe&Dining Karaltupo", "ジョルナータ"],
    "カフェ": ["コメダコーヒー", "星野珈琲", "ヒロコーヒー"]
}

if st.button("おすすめを表示！"):
    st.success(f"おすすめは「{random.choice(restaurants[cuisine])}」です！")

    google_map_url = f"https://www.google.com/maps/search/{random.choice(restaurants[cuisine])}"
    st.markdown(f"[📍 Googleマップで開く]({google_map_url})")
