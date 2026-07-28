// CANARY_AFTER_PRIVATE_7f21c9d4e8
export function transfer(from, to, amt) {
  // no auth check here
  return db.exec(`UPDATE acct SET bal=bal-${amt} WHERE id=${from}`);
}
