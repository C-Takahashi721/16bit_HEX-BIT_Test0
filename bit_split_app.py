import streamlit as st

def hex_to_bits(hex_str):
    try:
        value = int(hex_str, 16)
    except ValueError:
        return None
    bits = [(value >> i) & 1 for i in reversed(range(16))]
    return bits

st.title("16bit_HEXをBIT分割表示")

# 表示領域を広げるCSS
st.markdown(
    """
    <style>
        .block-container {
            max-width: 800px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

hex_input = st.text_input("16進数を入力（例: A5F3）", max_chars=4)

colors = ["#FFC0CB", "#ADD8E6", "#90EE90", "#FFFFE0"]  # 4色

if hex_input:
    bits = hex_to_bits(hex_input)
    if bits is not None:
        # HTMLテーブルを生成
        html = '<table style="border-collapse:collapse;"><tr>'
        for i, bit in enumerate(bits):
            color = colors[i // 4 % len(colors)]
            html += (
                f'<td style="background:{color}; '
                'padding:12px; border:1px solid #000; '
                'text-align:center; font-size:60px; color:#000;">'
                f'{bit}</td>'
            )
        html += '</tr><tr>'
        # ビット番号も表示（背景白・文字色黒・サイズ小さめ）
        for i in range(16):
            html += (
                '<td style="background:#fff; padding:2px;border:1px solid #000; font-size:18px; text-align:center; color:#000;">'
                f'BIT{15-i}</td>'
            )
        html += '</tr></table>'
        st.markdown(html, unsafe_allow_html=True)
    else:
        st.error("正しい16進数を入力してください（例: A5F3）")