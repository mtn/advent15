with import <nixpkgs> {};

stdenv.mkDerivation rec {
  name = "rust-environment";

  buildInputs = [
    cargo
    rustc
    rustfmt
  ];

  shellHook = ''
    export PATH=/home/mtn/.cargo/bin:$PATH
  '';
}
