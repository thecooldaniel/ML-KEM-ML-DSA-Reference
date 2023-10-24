REF_SRC := ./kyber-c/ref
REF_OBJ := ./ref_obj
CC := gcc
INCL := $(REF_SRC)
CFLAGS := -ggdb3 -O0

SOURCES := $(wildcard $(REF_SRC)/*.c)
OBJECTS := $(patsubst $(REF_SRC)/%.c, $(REF_OBJ)/%.o, $(SOURCES))

_DEPS = kex.c kem.c indcpa.c polyvec.c poly.c ntt.c cbd.c reduce.c verify.c fips202.c symmetric-shake.c randombytes.c
DEPS = $(patsubst %,$(REF_SRC)/%,$(_DEPS))

all:
	# $(CC) -I$(INCL) -L./kyber-c/ref $(CFLAGS) $(DEPS) kyber-c-testing.c -l:libpqcrystals_kyber512_ref.so -o kyber-c-testing.out
	$(CC) -I$(INCL) -L./kyber-c/ref $(CFLAGS) $(DEPS) kyber-c-testing.c -o kyber-c-testing.out

ref: $(OBJECTS)
	$(CC) $^ -o $@

$(REF_OBJ)/%.o: $(REF_SRC)/%.c
	$(CC) -I$(REF_SRC) -c $< -o $@

