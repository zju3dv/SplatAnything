"""Compatibility entry point. New commands use inference.py; legacy flags still work."""
from inference import load_config, main, parse_args

if __name__ == "__main__":
    main()
