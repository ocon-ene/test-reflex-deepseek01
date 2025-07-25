import reflex as rx

config = rx.Config(
    app_name="test_reflex_deepseek01",
    db_url="sqlite:///reflex.db", #using ORM object relational mapping
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ],
)