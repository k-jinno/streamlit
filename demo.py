import streamlit as st
import pandas as pd
import plotly.figure_factory as ff
import numpy as np
import time
import plotly.graph_objects as go

st.set_page_config(layout="wide")
def page1():
    st.title("Streamlitとは")
    st.write("StreamlitはPythonで簡単にWebアプリケーションを作成できるオープンソースのライブラリです。")
    st.write("Streamlitを使うことで、データの可視化や機械学習モデルのデバッグ、プロトタイプの作成など、様々な用途でWebアプリケーションを作成することができます。")
    st.link_button("Streamlit公式サイト", "https://streamlit.io/")
    st.write("その手軽さや便利さから、社内やグループ会社内でも業務で活用されています。")
    st.link_button("過去malee勉強会記事1", "https://malee.qiita.com/shimamura_at/items/0aff71593b0496d0cef4")
    st.link_button("過去malee勉強会記事2", "https://teams-share.qiita.com/shared_articles/6e8b63cc8dc0d0db1443e8cb6eee0b3f")
    st.link_button("docomoでの社内利用例", "https://it.impress.co.jp/articles/-/25986")
    st.write("10/30時点ではver1.39.0まで利用可能となっており、今回ver1.39.0で利用できる機能の中で応用的な機能を中心に紹介します。")
def page2():
    st.title("基本的な機能について")
    col1,col2 = st.columns(2)
    with col1:
        st.code('''
import streamlit as st
import pandas as pd
st.write("Hello *world!*") # 文字表示
df = pd.read_csv("data.csv")
st.dataframe(df)             # データフレーム表示
number = st.slider("好きな数字は？", 0, 100)  # スライダ選択
st.write(number) # 文字表示
uploaded_file = st.file_uploader("ファイルを選択してください") #ローカルファイル読み込み
color = st.color_picker("好きな色を選択してください", "#00F900") # カラーパレット
select_sports = st.radio("好きなスポーツは？",["野球", "サッカー", "テニス"]) # ラジオボタン
st.write(select_sports) # 文字表示
st.bar_chart(df,x="商品名",y="単価") # データ可視化
''',language="python")
    with col2:
        st.write("Hello *world!*")
        df = pd.read_csv("data.csv")
        st.dataframe(df)
        number = st.slider("好きな数字は？", 0, 100)
        st.write(number) # 文字表示
        uploaded_file = st.file_uploader("ファイルを選択してください")
        color = st.color_picker("好きな色を選択してください", "#00F900")
        select_sports = st.radio("好きなスポーツは？",["野球", "サッカー", "テニス"],)
        st.write(select_sports) # 文字表示
        st.bar_chart(df,x="商品名",y="単価")
def page3():
    st.title("最新機能について(1)")
    st.write("StreamlitはLLM利用時のデモアプリとしてもよく活用されます。")
    st.write("LLM関連のStreamlit機能として、以下の機能が存在しています。")
    st.write("他のLLMアプリ例は以下で紹介されています。")
    st.page_link("https://streamlit.io/generative-ai",label="公式サイトLLM利用例")
    test_txt = """Streamlitは、Pythonを使って簡単にWebアプリケーションを作成できるフレームワークです。
    特にデータの可視化や分析に強みがあり、データサイエンティストやエンジニアにとって非常に便利なツールです。
    主な特徴Pythonだけで開発可能: HTMLやCSSの知識が不要で、PythonコードだけでWebアプリを作成できます。
    美しいUI: 標準で綺麗なユーザーインターフェースが提供されており、簡単にグラフやチャートを追加できます。
    リアルタイム操作: グラフやデータのリアルタイム操作が可能で、インタラクティブなアプリケーションを作成できます。
"""
    def stream_data():
        yield "\n"
        for word in [t+"\n" if t=="。" else t for t in test_txt]:
            yield word + ""
            time.sleep(0.02)
    col1,col2 = st.columns(2)
    with col1:
        st.code('''
import streamlit as st
 # LLM利用時のプロンプト入力フォーマット
st.chat_input()
# 出力する文章に人間やロボットのアイコンを付与することで、LLMとの対応を表現する
# 'user', 'assistant', 'ai', 'human'から選択できる
st.chat_message()
# 任意の処理が完了するまで、待機状態を表示させる
st.spinner()
 # 文章の出力をLLMからの出力っぽく表現する
st.write_stream()
''',language="python")
    with col2:
            # st.write("Streamlitについて紹介してください")
        if prpmpt := st.chat_input():
            with st.chat_message('human'):
                st.markdown(prpmpt)
            with st.spinner('待機中...'):
                time.sleep(5)
            with st.chat_message('ai'):
                st.write_stream(stream_data)
def page4():
    st.title("最新機能について(2)")
    st.write("Streamlitはデータの可視化の面でも便利な機能があります")
    col1,col2 = st.columns(2)
    with col1:
        st.code('''
import streamlit as st
# 編集可能なデータフレームの提供
st.data_editor()
# Plotlyで作成したオブジェクトの利用
st.plotly_chart()
                ''')
    with col2:
        df = pd.read_csv("data.csv")
        edit_df = st.data_editor(df)
        st.write("編集後データの可視化")
        st.bar_chart(edit_df,x="商品名",y="単価")
        # Add histogram data
        x1 = np.random.randn(200) - 2
        x2 = np.random.randn(200)
        x3 = np.random.randn(200) + 2
        # Group data together
        hist_data = [x1, x2, x3]
        group_labels = ['Group 1', 'Group 2', 'Group 3']
        # Create distplot with custom bin_size
        fig = ff.create_distplot(
                hist_data, group_labels, bin_size=[.1, .25, .5])
        # Plot!
        st.plotly_chart(fig, use_container_width=True)
        df_airports = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2011_february_us_airport_traffic.csv')
        df_airports.head()
        df_flight_paths = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2011_february_aa_flight_paths.csv')
        df_flight_paths.head()
        fig = go.Figure()
        fig.add_trace(go.Scattergeo(
            locationmode = 'USA-states',
            lon = df_airports['long'],
            lat = df_airports['lat'],
            hoverinfo = 'text',
            text = df_airports['airport'],
            mode = 'markers',
            marker = dict(
                size = 2,
                color = 'rgb(255, 0, 0)',
                line = dict(
                    width = 3,
                    color = 'rgba(68, 68, 68, 0)'
                )
            )))
        flight_paths = []
        for i in range(len(df_flight_paths)):
            fig.add_trace(
                go.Scattergeo(
                    locationmode = 'USA-states',
                    lon = [df_flight_paths['start_lon'][i], df_flight_paths['end_lon'][i]],
                    lat = [df_flight_paths['start_lat'][i], df_flight_paths['end_lat'][i]],
                    mode = 'lines',
                    line = dict(width = 1,color = 'red'),
                    opacity = float(df_flight_paths['cnt'][i]) / float(df_flight_paths['cnt'].max()),
                )
            )
        fig.update_layout(
            title_text = 'Feb. 2011 American Airline flight paths<br>(Hover for airport names)',
            showlegend = False,
            geo = dict(
                scope = 'north america',
                projection_type = 'azimuthal equal area',
                showland = True,
                landcolor = 'rgb(243, 243, 243)',
                countrycolor = 'rgb(204, 204, 204)',
            ),
        )
        st.plotly_chart(fig)
def page5():
    st.title("最新機能について(3)")
    st.write("Streamlitにおけるレイアウト機能についても様々な機能があります")
    col1,col2 = st.columns(2)
    with col1:
        st.code('''
import streamlit as st
# サイドバー上にオブジェクトを配置
st.sidebar.**
                ''')
    with col2:
        st.sidebar.selectbox("選択",[1,2,3])
pg = st.navigation([
    st.Page(page1, title="Streamlitとは", icon="❓"),
    st.Page(page2, title="基本的な機能について", icon="📚"),
    st.Page(page3, title="最新機能について(1)", icon="🤖"),
    st.Page(page4, title="最新機能について(2)", icon="🤖"),
    st.Page(page5, title="最新機能について(3)", icon="🤖"),
])
pg.run()