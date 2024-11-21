# Let's Quiz

### [letsquiz.pythonanywhere.com/](https://letsquiz.pythonanywhere.com/) [![Website letsquiz.pythonanywhere.com](https://img.shields.io/website-up-down-green-red/http/letsquiz.pythonanywhere.com.svg)](http://letsquiz.pythonanywhere.com/)

Bu loyiha Django veb-platformasida ishlab chiqilgan onlayn test tashkil qilish veb-sayti hisoblanadi.<br>
Frontend dizayn uchun Twitter Bootstrap4 kutubxonasidan foydalanilgan.

[![GitHub release](https://img.shields.io/github/release/izzatbekulkanov/lets-quiz.svg)](https://img.shields.io/bower/vpre/bootstrap.svg)
[![GitHub issues](https://img.shields.io/github/issues/izzatbekulkanov/lets-quiz.svg)](https://github.com/izzatbekulkanov/lets-quiz/issues)
[![GitHub forks](https://img.shields.io/github/forks/izzatbekulkanov/lets-quiz.svg)](https://github.com/izzatbekulkanov/lets-quiz/network)
[![GitHub stars](https://img.shields.io/github/stars/izzatbekulkanov/lets-quiz.svg)](https://github.com/izzatbekulkanov/lets-quiz/stargazers)
[![GitHub license](https://img.shields.io/github/license/izzatbekulkanov/lets-quiz.svg)](https://github.com/izzatbekulkanov/lets-quiz/blob/master/LICENSE)
[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)

## Hozirgi funksiyalar

### Saytga kirish funksiyalari:

- Foydalanuvchi testga kirish uchun tizimga kirgan bo‘lishi kerak.
- Ro‘yxatdan o‘tishda _foydalanuvchi nomi_, _ism_, _familiya_, _e-mail manzil_ va _parol_ kerak bo‘ladi.
- Tizimga kirishda esa faqat _foydalanuvchi nomi_ va _parol_ talab qilinadi.

### Test funksiyalari:

- Barcha savollar tanlovli (multiple choice) savollardan iborat.
- Har bir savol foydalanuvchi uchun faqat bir marta ko‘rsatiladi.
- Savollar har bir foydalanuvchi uchun tasodifiy tartibda ko‘rsatiladi.
- Agar foydalanuvchi yangilash tugmasini bosib yuborsa yoki avvalgi sahifaga qaytsa, yangi savol ko‘rsatiladi va avvalgi savol qabul qilingan deb belgilanadi.
- Har bir javobdan so‘ng foydalanuvchiga javob to‘g‘ri yoki noto‘g‘ri ekanligi haqida xabar ko‘rsatiladi.

### Reyting (Leaderboard) funksiyalari:

- Reyting ro‘yxati foydalanuvchilar olgan ballar bo‘yicha tartiblanadi.
- Agar ikki foydalanuvchining ballari bir xil bo‘lsa, avval ro‘yxatdan o‘tgan foydalanuvchi yuqoriroq o‘rinni egallaydi.
- Reyting ro‘yxati hammaga ochiq. Kirish talab qilinmaydi.

### Ma’muriy funksiyalar:

- Faqat administrator savollar qo‘shishi mumkin.
- Admin savollarni qo‘shib, _"Chop etilgan"_ deb belgilangunga qadar ularni tahrirlashi mumkin.
- Chop etilgan savollarni o‘zgartirish yoki ularga kirish imkoni yo‘q. Admin faqat savollar ro‘yxatini ko‘rishi mumkin.
- Admin savollarni matn yoki tanlov bo‘yicha qidirishi mumkin.
- Admin savollarni chop etilgan yoki chop etilmagan holati bo‘yicha filtrlashi mumkin.

---

## Dasturlashni boshlash

Talablar:

- Python 3.6.x
- Django 1.11.x
- Ubuntu 17.04 yoki undan keyingi versiyalar, yoki Linux Mint 18.2 yoki undan keyingi versiyalar

### 1. Ushbu repozitoriyani klonlang

```bash
git clone https://github.com/izzatbekulkanov/DJANGO-QUIZ.git
cd lets_quiz
```
## `lets_quiz` katalogida quyidagi buyruqni ishga tushiring
pipenv shell

