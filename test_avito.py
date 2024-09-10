from playwright.sync_api import Page, sync_playwright


def choose_filter_category(page: Page, filter: str):
    page.click('//*[@id="root"]/div/div[3]/div/div[2]/div[2]/div')  # Фильтр категории
    page.get_by_title(filter).click()
    page.wait_for_load_state('networkidle')


def choose_game_and_back(page: Page, gamenum: int):
    page.click(f'//*[@id="root"]/div/div[5]/div[2]/div/ul/li[{gamenum}]/div/div')  # Карточка игры
    page.wait_for_load_state('networkidle')
    page.click(f'//*[@id="root"]/div/div[3]/div/div/div[5]/div/button') # Кнопка back to main
    page.wait_for_load_state('networkidle')


def get_last_page_number(page):
    xpath = '//*[@id="root"]/div/div[5]/div[1]/ul/li[8]'
    last_page_number = page.get_attribute(xpath, 'title')
    return int(last_page_number)


def select_button_by_number(page: Page, pagenum:int):
    page.click(f'//*[@id="root"]/div/div[5]/div[1]/ul/li[{pagenum}]')  # Кнопка страницы
    page.wait_for_load_state('networkidle')


def test_filter_by_category():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        url = "https://makarovartem.github.io/frontend-avito-tech-test-assignment/"
        page.goto(url)
        page.wait_for_load_state('networkidle')

        choose_filter_category(page, "mmorpg")
        choose_filter_category(page, "shooter")
        choose_filter_category(page, "strategy")
        choose_filter_category(page, "moba")
        choose_filter_category(page, "racing")
        choose_filter_category(page, "sports")
        choose_filter_category(page, "social")

        browser.close()


def test_back_button():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        url = "https://makarovartem.github.io/frontend-avito-tech-test-assignment/"
        page.goto(url)
        page.wait_for_load_state('networkidle')
        for i in range(10):
            choose_game_and_back(page, i+1)
            page.wait_for_timeout(1000)
        browser.close()


def test_pagination():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        url = "https://makarovartem.github.io/frontend-avito-tech-test-assignment/"
        page.goto(url)
        page.wait_for_load_state('networkidle')
        n = get_last_page_number(page)
        m = 5
        for i in range(4):
            select_button_by_number(page, i + 3)
        while m < n:
            select_button_by_number(page, 7)
            m += 1
        select_button_by_number(page, 8)
        while n != 0:
            select_button_by_number(page, 1)
            n -= 1
        browser.close()