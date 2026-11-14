app:
	streamlit run Gacha_Reviews\app\frontend\main.py

	strealit run Gacha_Reviews\app\frontend\report.py

	streamlit run Gacha_Reviews\app\frontend\graphs.py


train_sent:
	python -m Gacha_Reviews.app.sentiment_and_topic.train.py