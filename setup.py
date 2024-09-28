from setuptools import setup, find_packages

setup(
    name="brain_games",
    version="0.2.0",
    packages=find_packages(include=["brain_games", "brain_games.*"]),
    entry_points={
        "console_scripts": [
            "brain-games = brain_games.scripts.brain_games:main",
            "brain-even = brain_games.scripts.brain_even:main",
            "brain-calc = brain_games.scripts.brain_calc:main",
            "brain-gcd = brain_games.scripts.brain_gcd:main",
            "brain-progression = brain_games.scripts.brain_progression:main",
            "brain-prime = brain_games.scripts.brain_prime:main",
        ],
    },
    install_requires=[
        "prompt==0.4.1",  # или другие зависимости, которые нужны для проекта
    ],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
