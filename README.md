# start

```bash
## venvモジュールを使って、myenvという名前の仮想環境を作成します。仮想環境はPythonパッケージをプロジェクトごとに分離して管理する仕組みです。
python3 -m venv myenv
## 作成した仮想環境を有効化します。有効化すると、以降のコマンドで使用するPythonやpipが仮想環境内のものに切り替わります。
source myenv/bin/activate
```

```bash
python manage.py migrate

---
(myenv) yuumiiida@yuuminoMacBook-Pro myproject % python manage.py migrate

Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
(myenv) yuumiiida@yuuminoMacBook-Pro myproject %
```

```bash
## Djangoの開発用サーバーを起動しています。これにより、ローカルホスト（デフォルトは http://127.0.0.1:8000/）でDjangoアプリケーションをテストできます。
python manage.py runserver
```

以下にブラウザでアクセス

```bash
http://127.0.0.1:8000/
```

# admin

```bash
c-admin startproject myproject
```

```bash
python manage.py createsuperuser

Username (leave blank to use 'yuumiiida'): yuumiiida
Email address: idaten7240@gmail.com
Password:Tomato13
Password (again):Tomato13
Superuser created successfully.
```
