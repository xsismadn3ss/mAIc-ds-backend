import uvicorn
from src.utils.start_msg import hello


def main():
    hello()
    uvicorn.run(
        app="src.main:app",
        host="0.0.0.0",
        port=8000,
        log_level="info",
        reload=True,
    )

if __name__ == '__main__':
    main()