# python_django


## 💻 開発環境

- pipenv
- Python 3.8
- django 3.0.3
- selenium 3.141.0
  - geckordriver 0.26.0 (Win64)
- pytest
  - pytest-watch
- VSCode


## 💻 プロジェクト作成～テスト準備

`pipenv shell` で仮想環境に入ったところからスタート

```
pipenv shell

# プロジェクト作成
django-admin startproject mysite

cd mysite
```


- 最初のテスト（Red）
    ```
    pytest test_function.py
    ```
    - Webサーバ起動前のため、エラー。(Red)


- 最初のテスト（Green）
    ```
    # Webサーバ起動
    python manage.py runserver
    ```

    ```
    $ pytest test_function.py
    ============================= test session starts =============================
    platform win32 -- Python 3.8.1, pytest-5.3.5, py-1.8.1, pluggy-0.13.1
    rootdir: ....(パス：省略)....\mysite
    collected 1 item

    test_function.py .                                                       [100%]

    ============================= 1 passed in 22.19s ==============================
    ```
    - ローカルWebサーバで、djangoスタートページが起動。(Green)

    ![django](https://user-images.githubusercontent.com/33124627/74706776-30a76600-525b-11ea-80ce-e85dfa17bbb1.png)

