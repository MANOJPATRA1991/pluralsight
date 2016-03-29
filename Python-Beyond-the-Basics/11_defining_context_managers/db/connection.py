# -*- coding: utf-8 -*-

import contextlib

from .transaction import Transaction


class Connection:

    def __init__(self):
        self.xid = 0

    def _start_transaction(self):
        print('starting transaction', self.xid)
        rslt = self.xid
        self.xid += 1
        return rslt

    def _commit_transaction(self, xid):
        print('committing transaction', xid)

    def _rollback_transaction(self, xid):
        print('rolling back transaction', xid)


@contextlib.contextmanager
def start_transaction(connection):
    tx = Transaction(connection)

    try:
        yield tx
    except:
        tx.rollback()
        raise

    tx.commit()
