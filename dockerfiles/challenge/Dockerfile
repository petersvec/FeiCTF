FROM petersvec/ctf

RUN apt-get update

WORKDIR /home/ctf

COPY flag /flag
COPY vuln /vuln
COPY .gdbinit /home/ctf

RUN chown root:root /flag
RUN chmod 400 /flag
RUN chown root:root /vuln
RUN chmod 4705 /vuln

USER ctf

CMD ["/bin/bash"]
