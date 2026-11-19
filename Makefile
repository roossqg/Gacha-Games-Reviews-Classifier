app:
	streamlit run Gacha_Reviews\app\frontend\main.py

	strealit run Gacha_Reviews\app\frontend\report.py

	streamlit run Gacha_Reviews\app\frontend\graphs.py


train_sent:
	python -m Gacha_Reviews.app.sentiment_and_topic.train.py
	python -m Gacha_Reviews.app.sentiment_and_topic.vader_sentiment_classification.py
	python -m Gacha_Reviews.app.sentiment_and_topic.test.py
	python -m Gacha_Reviews.app.sentiment_and_topic.evaluation.py
	python -m Gacha_Reviews.tests.py
	pytest -m Gacha_Reviews\tests.analytics.test_analyst_session.py