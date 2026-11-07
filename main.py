import re

def remove_html_tags(text):
    # Регулярное выражение: <.*?> 
    # <  - начало тега
    # .* - любые символы
    # ?  - не жадный поиск (останавливается на первом закрывающем >)
    # >  - конец тега
    clean_text = re.sub(r'<.*?>', '', text)
    
    # Убираем лишние пробелы, которые могли образоваться после удаления тегов
    clean_text = re.sub(r'\s+', ' ', clean_text).strip()
    
    return clean_text

# Тестирование
if __name__ == "__main__":
    html_text = "<h1>Привет, мир!</h1><p>Это <b>тестовый</b> текст с <a href='#'>ссылкой</a>.</p>"
    print("Исходный текст:")
    print(html_text)
    print("\nТекст без HTML-тегов:")
    print(remove_html_tags(html_text))