import streamlit as st
import random
import urllib.parse

# ✅ ページ設定（← これを最初に追加！）
st.set_page_config(
    page_title="レストランピッカー",        # タブのタイトル
    page_icon="restaurant-picker3.png",       # タブのアイコン画像
    layout="centered"
)

# 小さめのタイトル（HTMLを使ってサイズ変更）
st.markdown("<h3 style='text-align: left;'>🍽 今日のお店を決めよう</h3>", unsafe_allow_html=True)

# ジャンル選択
cuisine = st.radio("ジャンルを選んでください", ["居酒屋", "洋食屋", "カフェ"])

# 店リスト
restaurants = {
    "居酒屋": ["海鮮居酒屋天秤棒玉造店", "居酒屋大御所", "大衆酒場タムヤ"],
    "洋食屋": ["トロイカ＆リビエラ", "カフェ&ダイニングカラッポ", "ジョルナータ"],
    "カフェ": ["コメダコーヒー", "星野珈琲", "ヒロコーヒー", "サンマルクカフェ", "スターバックス"]
}

# ボタン押下で実行
if st.button("おすすめを表示！"):
    shop = random.choice(restaurants[cuisine])
    st.success(f"おすすめは「{shop}」です！")

    encoded_shop = urllib.parse.quote(shop)
    google_map_url = f"https://www.google.com/maps/search/?api=1&query={encoded_shop}"
    st.markdown(f"[📍 Googleマップで開く]({google_map_url})")
    
# （おまけ）アイコン画像をアプリ内にも表示
st.image("restaurant-picker3.png", width=360)
