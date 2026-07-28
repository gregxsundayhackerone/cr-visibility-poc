import logging
import sqlite3

logger = logging.getLogger(__name__)


def record_settlement(conn: sqlite3.Connection, batch_id: str, total_cents: int) -> None:
    logger.info("recording settlement %s total=%s", batch_id, total_cents)
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO audit_log (actor, action, payload) VALUES (?, ?, ?)",
        ("system", "settlement", f"{batch_id}:{total_cents}"),
    )
    conn.commit()
    logger.info("settlement recorded %s", batch_id)
