from infi.clickhouse_orm import migrations

operations = [
    migrations.RunSQL(
        """ CREATE MATERIALIZED VIEW events_daily_summary
            ENGINE = SummingMergeTree
            PARTITION BY toYYYYMM(date) ORDER BY (tid, cn, date)
            POPULATE
            AS SELECT
                toStartOfDay(event_date) AS date,
                tid,
                cn,
                countIf(t='pageview') as pageviews,
                countIf(t='event' AND ec='Outbound Link' AND ea='click') as clicks,
                clicks / pageviews as ctr,
                ctr * 100 as ctr_perc,
                sumIf(r, t='revenue') as revenue
            FROM events
            GROUP BY tid, cn, date
        """
    )
]
