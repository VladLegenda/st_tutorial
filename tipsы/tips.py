import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import streamlit as st

# Настройка страницы
st.title("Анализ чаевых")
st.sidebar.header("Настройки")

# Загрузка файла
uploaded_file = st.sidebar.file_uploader("Загрузите CSV файл", type=["csv"])

if uploaded_file is not None:
    tips = pd.read_csv(uploaded_file)
    
    # Отображение первых строк датафрейма
    st.write("Первые строки датасета:")
    st.write(tips.head())

    #  Создание столбца time_order
    start_date = '2023-01-01'
    end_date = '2023-01-31'
    tips['time_order'] = pd.to_datetime(np.random.choice(pd.date_range(start_date, end_date), size=len(tips)))

    #  График динамики чаевых во времени
    tips_grouped = tips.groupby('time_order')['tip'].sum().reset_index()
    plt.figure(figsize=(12, 6))
    plt.plot(tips_grouped['time_order'], tips_grouped['tip'], marker='o', color='blue')
    plt.title('Динамика чаевых во времени', fontsize=16)
    plt.xlabel('Дата', fontsize=14)
    plt.ylabel('Сумма чаевых', fontsize=14)
    plt.xticks(rotation=45)
    plt.grid()
    st.pyplot(plt)

    #  Гистограмма total_bill
    plt.figure(figsize=(12, 6))
    plt.hist(tips['total_bill'], bins=20, color='skyblue', edgecolor='black')
    plt.title('Гистограмма total bill')
    plt.xlabel('Общий счёт')
    plt.ylabel('Частота')
    plt.grid()
    st.pyplot(plt)

    #  Scatterplot между total_bill и tip
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=tips, x='total_bill', y='tip', color='blue', alpha=0.7)
    plt.title('Связь между общим счётом и чаевыми', fontsize=16)
    plt.xlabel('Общий счёт', fontsize=14)
    plt.ylabel('Чаевые', fontsize=14)
    plt.grid()
    st.pyplot(plt)

    #  Scatter plot с размером группы
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=tips, x='total_bill', y='tip', size='size', sizes=(20, 200), alpha=0.5, hue='sex')
    plt.title('Связь между общим счётом, чаевыми и размером компании', fontsize=16)
    plt.xlabel('Общий счёт', fontsize=14)
    plt.ylabel('Чаевые', fontsize=14)
    plt.grid()
    st.pyplot(plt)

    #  Средний общий счёт по дням недели
    plt.figure(figsize=(12, 6))
    sns.barplot(data=tips, x='day', y='total_bill', ci=None, palette='pastel')
    plt.title('Средний общий счёт по дням недели', fontsize=16)
    plt.xlabel('День недели', fontsize=14)
    plt.ylabel('Средний общий счёт', fontsize=14)
    plt.grid()
    st.pyplot(plt)

    #  Scatter plot чаевых по дням недели
    plt.figure(figsize=(12, 6))
    sns.scatterplot(data=tips, x='tip', y='day', hue='sex', palette='deep', style='smoker', markers={'Yes': 'o', 'No': 'X'})
    plt.title('Чаевые по дням недели', fontsize=16)
    plt.xlabel('Чаевые', fontsize=14)
    plt.ylabel('День недели', fontsize=14)
    plt.legend(title='Пол и курение')
    plt.grid()
    st.pyplot(plt)

    #  Box plot по дням и времени
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=tips, x='day', y='total_bill', hue='time', palette='pastel')
    plt.title('Сумма всех счетов за каждый день, разбивая по time (Dinner/Lunch)', fontsize=16)
    plt.xlabel('День недели', fontsize=14)
    plt.ylabel('Общий счёт', fontsize=14)
    plt.grid()
    st.pyplot(plt)

    #  Гистограммы чаевых на обед и ужин
    plt.figure(figsize=(12, 6))
    sns.histplot(data=tips[tips['time'] == 'Lunch'], x='tip', bins=20, color='lightgreen', label='Обед', kde=True)
    sns.histplot(data=tips[tips['time'] == 'Dinner'], x='tip', bins=20, color='salmon', label='Ужин', kde=True)
    plt.title('Гистограммы чаевых на обед и ужин', fontsize=16)
    plt.xlabel('Чаевые', fontsize=14)
    plt.ylabel('Частота', fontsize=14)
    plt.legend()
    plt.grid()
    st.pyplot(plt)

    #  Тепловая карта зависимостей
    numeric_tips = tips.select_dtypes(include=['float64', 'int64'])
    correlation_matrix = numeric_tips.corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', square=True, cbar_kws={"shrink": .8})
    plt.title('Тепловая карта зависимостей численных переменных', fontsize=16)
    st.pyplot(plt)

    #  Влияние общего счета на чаевые
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=tips, x='total_bill', y='tip', hue='time', palette='coolwarm', alpha=0.7)
    plt.title('Влияние общего счета на чаевые в зависимости от времени', fontsize=16)
    plt.xlabel('Общий счёт', fontsize=14)
    plt.ylabel('Чаевые', fontsize=14)
    plt.grid()
    st.pyplot(plt)
