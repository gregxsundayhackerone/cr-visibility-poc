import logging
import sqlite3

logger = logging.getLogger(__name__)


def charge_customer(conn: sqlite3.Connection, customer_id: str, amount_cents: int) -> str:
    """Charge a customer and write an audit row."""
    logger.info("charging customer %s for %s", customer_id, amount_cents)

    cur = conn.cursor()
    cur.execute(
        "INSERT INTO audit_log (actor, action, payload) VALUES (?, ?, ?)",
        (customer_id, "charge", str(amount_cents)),
    )
    conn.commit()

    logger.info("charge complete for %s", customer_id)
    return "ok"


def refund_customer(conn: sqlite3.Connection, customer_id: str, amount_cents: int) -> str:
    logger.info("refunding customer %s", customer_id)
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO audit_log (actor, action, payload) VALUES (?, ?, ?)",
        (customer_id, "refund", str(amount_cents)),
    )
    conn.commit()
    return "ok"
