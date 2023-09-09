# pip install streamlit
# streamlit hello
# streamlit run main.py でローカルURL

import streamlit as st
# import numpy as np
# import pandas as pd
# from PIL import Image
import time


# titleを指定
st.title('Streamlit 超入門')

st.sidebar.write('プログレスバーの表示')
'Start!!'

# 空を追加
latest_iteration = st.empty()
bar = st.progress(0)

# 上のバーの上の領域に、変化を表示させる。time.sleepで速度指定
for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!!!!!'


# imageを表示(use_column_width で画面に合わせて表示)
# checkbox でtrue/false により画像を表示非表示も出来る。

# if st.checkbox('Show Image'):
#     img = Image.open('angry.png')
#     st.image(img, caption='gazou', use_column_width=True)

# option = st.selectbox(
#    '貴方が好きな数字を教えてください。',
#    list(range(1, 11))
# )

# '貴方の好きな数字は、', option, 'です。'


left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

ecpander1 = st.expander('問い合わせ1')
ecpander1.write('問い合わせ1の解答')
ecpander2 = st.expander('問い合わせ2')
ecpander2.write('問い合わせ2の解答')
ecpander3 = st.expander('問い合わせ3')
ecpander3.write('問い合わせ3の解答')


# st.sidebar でバーを追加。
# text = st.text_input('貴方が好きな趣味を教えてください。')
# condition = st.slider('貴方の今の調子は？', 0, 100, 50)

# '貴方の趣味', text
# 'コンディション:', condition


# 乱数を出し、割った数値に出したい緯度経度の数値を足す
# df = pd.DataFrame(
#   np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
#   columns=['lat', 'lon']
# )

# writeでも表は出せるが、縦横を指定できるのはdataframeのみ。
# 動的な表 dataframe, 静的な表 table

# st.dataframe(df.style.highlight_max(axis=0))


# dfを折れ線グラフ化 line_chart, 範囲を色付け area_chart, 棒グラフ bar_chart 
# 地図を出力 map
# st.map(df)


# 文字列""" """, markdown可能
"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""
