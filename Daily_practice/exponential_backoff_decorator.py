import time

def retry(max_attempts):
    def decorator(func):
        def wrapper(*args, **kwargs):
            delay = 1
            for attempt in range(max_attempts):
                try:
                    print(f"Attempt {attempt + 1}")
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Error: {e}, retrying in {delay} seconds...")
                    time.sleep(delay)
                    delay += 2
            raise Exception("Failed after retries")
        return wrapper
    return decorator


# APPLY DECORATOR
@retry(max_attempts=5)
def unstable_function():
    raise ValueError("Always failing!")


# 🔥 CALL FUNCTION
result = unstable_function()
print("Final Result:", result)