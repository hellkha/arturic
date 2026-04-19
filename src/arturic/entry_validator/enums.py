from enum import Enum


class Department(str, Enum):
    MDR = "MDR"
    SA = "SA"
    WB = "WB"


class Processor(str, Enum):
    JAMES_L = "James.L"
    NORA_K = "Nora.K"
    ARTHUR_B = "Arthur.B"
    LENA_P = "Lena.P"
    FELIX_G = "Felix.G"
    DR_VOSS = "Dr.Voss"
    CLARA_M = "Clara.M"


class Bin(str, Enum):
    GR = "GR"  # Grief
    BL = "BL"  # Bliss
    AX = "AX"  # Anxiety
    SP = "SP"  # Spite


class Category(str, Enum):
    ALPHA = "alpha"
    BETA = "beta"
    GAMMA = "gamma"
    DELTA = "delta"
