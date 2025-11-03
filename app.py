import streamlit as st
import random

st.title("🍽 今日のお店を決めよう！")

cuisine = st.radio("ジャンルを選んでください", ["居酒屋", "洋食屋", "カフェ"])

restaurants = {
    "居酒屋": ["海鮮居酒屋天秤棒玉造店", "居酒屋大御所", "大衆酒場タムヤ"],
    "洋食屋": ["トロイカ＆リビエラ", "Cafe&DiningKaraltupo", "ジョルナータ"],
    "カフェ": ["コメダコーヒー", "星野珈琲", "ヒロコーヒー"]
}

if st.button("おすすめを表示！"):
    shop = random.choice(restaurants[cuisine])
    st.success(f"おすすめは「{shop}」です！")

    google_map_url = f"https://www.google.com/maps/search/{shop}"
    st.markdown(f"[📍 Googleマップで開く]({google_map_url})")
