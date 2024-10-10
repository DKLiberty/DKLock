#include <windows.h>
#include <string>
#include <commctrl.h>

#define PIN_CODE L"1309" // Задайте свой пин-код здесь

HHOOK hHook;
bool isAuthenticated = false;

LRESULT CALLBACK KeyboardHook(int nCode, WPARAM wParam, LPARAM lParam) {
    if (nCode == HC_ACTION) {
        KBDLLHOOKSTRUCT* pKb = (KBDLLHOOKSTRUCT*)lParam;

        // Проверка нажатия клавиши Win
        if (wParam == WM_KEYDOWN && pKb->vkCode == VK_LWIN) {
            return 1; // Блокируем
        }

        // Проверка нажатия Win+Tab или Win+D
        if ((wParam == WM_KEYDOWN) && (GetKeyState(VK_LWIN) & 0x8000)) {
            if (pKb->vkCode == VK_TAB || pKb->vkCode == 'D') {
                return 1; // Блокируем
            }
        }
    }
    return CallNextHookEx(hHook, nCode, wParam, lParam);
}

// Обработчик сообщений для окна
LRESULT CALLBACK WindowProc(HWND hwnd, UINT uMsg, WPARAM wParam, LPARAM lParam) {
    static HWND hEdit, hStatic; // Объявляем переменные здесь
    static int centerX, centerY;

    switch (uMsg) {
    case WM_CREATE:
        // Получение размеров окна
        RECT rect;
        GetClientRect(hwnd, &rect);
        centerX = (rect.right - rect.left) / 2;
        centerY = (rect.bottom - rect.top) / 2;

        // Создание надписи "Input PassWord"
        hStatic = CreateWindow(L"STATIC", L"Input PassWord", WS_VISIBLE | WS_CHILD | SS_CENTER | SS_NOTIFY,
            centerX - 100, centerY - 60, 200, 20, hwnd, NULL, NULL, NULL);

        // Установка шрифта и цвета текста
        SendMessage(hStatic, WM_SETFONT, (WPARAM)CreateFont(20, 0, 0, 0, FW_NORMAL, FALSE, FALSE, FALSE,
            DEFAULT_CHARSET, OUT_DEFAULT_PRECIS, CLIP_DEFAULT_PRECIS, DEFAULT_QUALITY,
            VARIABLE_PITCH, L"Segoe UI"), TRUE);

        // Создание поля ввода
        hEdit = CreateWindowEx(0, L"EDIT", L"", WS_CHILD | WS_VISIBLE | WS_BORDER | ES_PASSWORD | ES_CENTER,
            centerX - 100, centerY - 20, 200, 20, hwnd, NULL, NULL, NULL);

        // Установка символа для ввода
        SendMessage(hEdit, EM_SETPASSWORDCHAR, (WPARAM)L'x', 0); // Заменяем звездочку на икс

        // Создание кнопки
        CreateWindow(L"BUTTON", L"Unlock", WS_TABSTOP | WS_VISIBLE | WS_CHILD | BS_DEFPUSHBUTTON,
            centerX - 100, centerY + 20, 200, 30, hwnd, (HMENU)1, NULL, NULL);
        break;

    case WM_COMMAND:
        if (LOWORD(wParam) == 1) { // Если нажата кнопка "Unlock"
            wchar_t input[10];
            GetWindowText(hEdit, input, 10);
            if (wcscmp(input, PIN_CODE) == 0) {
                isAuthenticated = true; // Устанавливаем флаг аутентификации
                PostMessage(hwnd, WM_CLOSE, 0, 0); // Закрыть приложение
            }
            else {
                MessageBox(hwnd, L"Неверный PIN-код", L"Ошибка", MB_OK | MB_ICONERROR);
            }
        }
        break;


    case WM_KEYDOWN: // Обработка нажатия клавиш
        if (wParam == VK_RETURN) { // Если нажата клавиша Enter
            wchar_t input[10];
            GetWindowText(hEdit, input, 10); // Получаем текст из поля ввода
            if (wcscmp(input, PIN_CODE) == 0) { // Сравниваем с PIN-кодом
                isAuthenticated = true; // Устанавливаем флаг аутентификации
                PostMessage(hwnd, WM_CLOSE, 0, 0); // Закрыть приложение
            }
            else {
                MessageBox(hwnd, L"Неверный PIN-код", L"Ошибка", MB_OK | MB_ICONERROR);
            }
        }
        break;

    case WM_DESTROY:
        PostQuitMessage(0);
        return 0;

    case WM_CLOSE:
        if (!isAuthenticated) { // Если не аутентифицированы, игнорируем закрытие
            return 0; // Не закрываем окно
        }
        break;

    case WM_PAINT: {
        PAINTSTRUCT ps;
        HDC hdc = BeginPaint(hwnd, &ps);
        HBRUSH brush = CreateSolidBrush(RGB(0, 0, 0)); // Черный фон
        FillRect(hdc, &ps.rcPaint, brush);
        DeleteObject(brush); // Удаление кисти

        // Установка белого цвета текста
        SetTextColor(hdc, RGB(255, 255, 255)); // Белый цвет текста
        SetBkMode(hdc, TRANSPARENT); // Прозрачный фон для текста

        // Рисование текста "Input PassWord"
        TextOut(hdc, centerX - 90, centerY - 60, L"Input PassWord", 15);

        EndPaint(hwnd, &ps);
    }
                 break;
    }
    return DefWindowProc(hwnd, uMsg, wParam, lParam);
}

// Точка входа для приложения
int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE, LPSTR, int) {

    const wchar_t CLASS_NAME[] = L"DKLockWindowClass";

    WNDCLASS wc = {};
    wc.lpfnWndProc = WindowProc;
    wc.hInstance = hInstance;
    wc.lpszClassName = CLASS_NAME;

    RegisterClass(&wc);

    // Создание окна с флагами, блокирующими его
    HWND hwnd = CreateWindowEx(
        WS_EX_TOPMOST | WS_EX_TOOLWINDOW, CLASS_NAME, L"DKLock",
        WS_POPUP, 0, 0, GetSystemMetrics(SM_CXSCREEN), GetSystemMetrics(SM_CYSCREEN),
        NULL, NULL, hInstance, NULL
    );

    ShowWindow(hwnd, SW_SHOW);

    hHook = SetWindowsHookEx(WH_KEYBOARD_LL, KeyboardHook, NULL, 0); // Установка хука

    MSG msg; // Объявление переменной msg
    while (GetMessage(&msg, NULL, 0, 0)) {
        TranslateMessage(&msg);
        DispatchMessage(&msg);
    }

    UnhookWindowsHookEx(hHook); // Снятие хука

    return 0;
}
