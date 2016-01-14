# Packt Grabber

Claims today's free ebook from https://www.packtpub.com/packt/offers/free-learning for your account.

## Dependencies

You may need to Install following python packages:

```sh
pip install requests beautifulsoup4
```

## Configure

Edit 8 and 9 lines, write your email and password of packtpub account.

```python
email    = 'your@email'
password = 'your_password'
```

## Run daily

Add this lines to your crontab (run _crontab -e_) to run this script every day at midnight:
```
0 0 * * * python /path/to/packt-grabber/packt-grabber.py &>/dev/null
```
