# Python Django CRUD

django開発用テンプレート

- 機能要件
  - CRUD実装
  - API機能
- 非機能要件
  - XSS、SQLインジェクション等へのセキュリティ対策
- テスト（開発）
  - テスト自動化


## 💻 開発環境

- pipenv
- Python (3.8)
- django  (3.0.3)
- django-bootstrap4 (1.1.1)
- selenium (3.141.0)
  - geckordriver (0.26.0 / Win64)
- pytest
  - pytest-watch
- Visual Studio Code


## 💻 プロジェクト作成～テスト準備

- プロジェクト　`mysite/`

  `pipenv shell` で仮想環境に入ったところからスタート
  ```
  pipenv shell

  # プロジェクト作成
  django-admin startproject mysite

  cd mysite
  ```

#### テスト用に `Bash` を別途起動

テストは`test_function.py`に書いていく。

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

    - ローカルWebサーバで、djangoトップページが起動。(Green)

    ![django](https://user-images.githubusercontent.com/33124627/74706776-30a76600-525b-11ea-80ce-e85dfa17bbb1.png)

    - 以降、`ptw test_function.py` で自動テストを走らせながら開発。


---


## (※以降、on going)

  ![Image_ichiran](https://user-images.githubusercontent.com/33124627/75225335-bdb76580-57ed-11ea-82aa-36919d9af6f0.png)

  ![Image_add](https://user-images.githubusercontent.com/33124627/75225458-fc4d2000-57ed-11ea-847e-410c749c2b67.png)

---

## 💻 アプリケーション作成

- CRUD部分　`myapp/`
  ```
  python manage.py startapp myapp
  ```

- API部分　`api/`
  ```
  python manage.py startapp api
  ```
