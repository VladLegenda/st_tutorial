import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io
import plotly.express as px

# Заголовок приложения
st.title("Анализ котировок Apple и чаевых")

# Боковая панель
st.sidebar.header("Настройки")

# Загрузка данных о чаевых
uploaded_file = st.sidebar.file_uploader("Загрузите CSV файл с чаевыми", type=['csv'])

if uploaded_file is not None:
    try:
        tips_data = pd.read_csv(uploaded_file)
        
        # Статистика и график средних чаевых
        st.sidebar.subheader("Статистические показатели")
        st.sidebar.write(tips_data.describe())

        # Группировка данных по полу и средние чаевые
        average_tips = tips_data.groupby('sex')['tip'].mean()
        st.sidebar.subheader("Средние чаевые по полу")
        
        # Используем Plotly для графика
        fig = px.bar(x=average_tips.index, y=average_tips.values, labels={'x': 'Пол', 'y': 'Средние чаевые'},
                     title='Средние чаевые по полу')
        st.plotly_chart(fig)

        # Скачивание графика
        buf = io.BytesIO()
        fig.write_image(buf, format='png')
        buf.seek(0)

        st.sidebar.download_button(
            label="Скачать график средних чаевых",
            data=buf,
            file_name="average_tips_by_sex.png",
            mime="image/png"
        )
        
    except Exception as e:
        st.error(f"Ошибка при загрузке файла: {e}")
else:
    st.warning("Пожалуйста, загрузите CSV файл для анализа чаевых.")

# Котировки Apple
st.header("Котировки Apple")
start_date = st.sidebar.date_input("Выберите дату начала", value=pd.to_datetime('2014-01-01'))
end_date = st.sidebar.date_input("Выберите дату окончания", value=pd.to_datetime('2024-12-17'))

data = yf.download('AAPL', start=start_date, end=end_date)
st.line_chart(data['Close'])

# Скачивание котировок
csv_data = data.to_csv().encode('utf-8')
st.sidebar.download_button(
    label="Скачать котировки Apple",
    data=csv_data,
    file_name='apple_stock_data.csv',
    mime='text/csv'
)
