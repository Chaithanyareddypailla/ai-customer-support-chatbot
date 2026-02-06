import redis

r = redis.Redis(host="localhost", port=6379, decode_responses=True)

def save_message(user_id, message):
    r.lpush(user_id, message)

def get_history(user_id):
    return r.lrange(user_id, 0, 5)
