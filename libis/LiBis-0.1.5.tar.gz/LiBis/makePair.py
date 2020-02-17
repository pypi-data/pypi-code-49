import sys
import pysam

def makePair(filename):
  dict = {}
  multiname = {}
  with pysam.AlignmentFile(filename) as f:
    for line in f:
      if line.query_name not in multiname:
        multiname[line.query_name] = 1
      else:
        multiname[line.query_name] += 1
  f = pysam.AlignmentFile(filename)
  out = pysam.AlignmentFile(filename+'.pair.bam',"wb", template=f)
  for line in f:
    if multiname[line.query_name]==1:
      out.write(line)
      continue
    if line.query_name not in dict:
      dict[line.query_name] = [line]
    else:
      dict[line.query_name].append(line)
  f.close()
  del multiname
  for k,v in dict.items():
    if True:
      #line = v[0]
      #line.flag = line.flag&8
      #out.write(line)
      #else:
      #for l in v:
      #  #print(l.to_string())
      for i in range(len(v)):
        for j in range(i+1,len(v)):
          r1 = v[i]
          r1_mate = r1.get_tag('MT')
          r1_frag = r1.get_tag('FG')
          r1_chr = r1.reference_name
          r1_start = r1.reference_start
          r1_len = r1.reference_length

          r2 = v[j]
          r2_mate = r2.get_tag('MT')
          r2_frag = r2.get_tag('FG')
          r2_chr = r2.reference_name
          r2_start = r2.reference_start
          r2_len = r2.reference_length
          #print('r1:', r1_mate, r1_frag, r1_chr, r1_start, r1_len)
          #print('r2:', r2_mate, r2_frag, r2_chr, r2_start, r2_len)
          if r1_mate!=r2_mate:
            r1_end = r1_start + r1_len
            r2_end = r2_start + r2_len
            if r1_chr==r2_chr:
              template_length = max(r1_end, r2_end) - min(r1_start, r2_start)
              #print(template_length, r1.next_reference_start, r2.next_reference_start)
              if template_length<r1.template_length or r1.next_reference_start<0:
                r1.template_length = template_length
                r1.next_reference_name = r2_chr
                r1.next_reference_start = r2_start 
                if r1_mate==1:
                  m_info=64
                else:
                  m_info=128
                if r2.flag&16>0:
                  r1.flag = r1.flag|32
                r1.flag = r1.flag|1
                r1.flag = r1.flag|m_info
                #print('Updated r1:', r1.to_string())
              if template_length<r2.template_length or r2.next_reference_start<0: 
                r2.template_length = template_length
                r2.next_reference_name = r1_chr
                r2.next_reference_start = r1_start 
                if r2_mate==1:
                  m_info=64
                else:
                  m_info=128
                if r1.flag&16>0:
                  r2.flag = r2.flag|32
                r2.flag = r2.flag|1
                r2.flag = r2.flag|m_info
                #print('Updated r2:', r2.to_string())
            else:
              if r1.next_reference_start<0:
                r1.next_reference_name = r2_chr
                r1.next_reference_start = r2_start 
                if r1_mate==1:
                  m_info=64
                else:
                  m_info=128
                if r2.flag&16>0:
                  r1.flag = r1.flag|32
                r1.flag = r1.flag|1
                r1.flag = r1.flag|m_info
              if r2.next_reference_start<0: 
                r2.next_reference_name = r1_chr
                r2.next_reference_start = r1_start 
                if r2_mate==1:
                  m_info=64
                else:
                  m_info=128
                if r1.flag&16>0:
                  r2.flag = r2.flag|32
                r2.flag = r2.flag|1
                r2.flag = r2.flag|m_info
      for line in v: 
        out.write(line)
      #print('=============================================')

  out.close()

          
if __name__=="__main__":
  makePair(sys.argv[1])



