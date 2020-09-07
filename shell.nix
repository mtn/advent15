with import <nixpkgs> {};

stdenv.mkDerivation rec {
  name = "rust-environment";

  buildInputs = [
    cargo
    rustc
  ];
}
